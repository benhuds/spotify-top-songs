import requests
import json

def getTopSongs(offset, hs):

    topSongsUrl = "https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=50&offset=" + str(offset)

    try:
        r = requests.get(topSongsUrl, headers=hs, allow_redirects=False)
        uriList = []
        for i in r.json()['items']:
            uriList.append(i['uri'])
        return uriList

    except:
        print "Failed with status code: " + str(r.status_code)

def createPlaylist(name, hs):

    createPlaylistUrl = "https://api.spotify.com/v1/me/playlists"

    try:
        print "Creating playlist named: " + name
        r = requests.post(createPlaylistUrl, headers=hs, allow_redirects=False, data=json.dumps({"name": name}))
        playlistId = r.json()['id']
        print "Success! Created playlist with ID " + playlistId
        return playlistId

    except:
        print "Failed with status code: " + str(r.status_code)

def addTracks(playlistId, uris, hs):
        
    addTracksUrl = "https://api.spotify.com/v1/playlists/" + playlistId + "/tracks"

    try:
        print "Adding tracks to playlist..."
        r = requests.post(addTracksUrl, headers=hs, allow_redirects=False, data=json.dumps({"uris": uris}))
        print "Success! Added " + str(len(uris)) + " tracks to playlist " + playlistId
        return

    except:
        print "Failed with status code: " + r.status_code

if __name__ == "__main__":

    headers = {
        'authorization': "Bearer " + "your-token-here",
        'content-type': "application/json",
    }

    # Create playlist
    playlistName = "Your Top Songs of the Decade"
    playlist = createPlaylist(playlistName, headers)

    # Add your top 100 tracks to the playlist you just created
    addTracks(playlist, getTopSongs(0, headers), headers)
    addTracks(playlist, getTopSongs(49, headers), headers)

