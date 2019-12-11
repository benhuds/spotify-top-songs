import requests
import json

def getTopSongs(offset, hs):

    topSongsUrl = "https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=50&offset=" + str(offset)

    r = requests.get(topSongsUrl, headers=hs, allow_redirects=False)

    uriList = []

    for i in r.json()['items']:
        uriList.append(i['uri'])

    return uriList

def createPlaylist(name, hs):

    createPlaylistUrl = "https://api.spotify.com/v1/me/playlists"

    playlistParams = {"name": name}

    try:
        print "Creating playlist named: " + name
        r = requests.post(createPlaylistUrl, headers=hs, allow_redirects=False, data=json.dumps(playlistParams))
        playlistId = r.json()['id']
        print "Success! Created playlist with ID " + playlistId

    except:
        print "Failed with status code: " + str(r.status_code)

    return playlistId

def addTracks(playlistId, uris, hs):
        
    addTracksUrl = "https://api.spotify.com/v1/playlists/" + playlistId + "/tracks"

    trackParams = {"uris": uris}

    try:
        print "Adding tracks to playlist..."
        r = requests.post(addTracksUrl, headers=hs, allow_redirects=False, data=json.dumps(trackParams))
        print "Success! Added " + str(len(uris)) + " tracks to playlist " + playlistId

    except:
        print "Failed with status code: " + r.status_code

    return

if __name__ == "__main__":

    headers = {
        'authorization': "Bearer " + "your-token-here",
        'content-type': "application/json",
    }

    # Create playlist
    playlistName = "Your Top Songs of the Decade"
    playlist = createPlaylist(playlistName, headers)

    # Get your top 100 songs
    uri1 = getTopSongs(0, headers)
    uri2 = getTopSongs(49, headers)

    # Add the tracks to the playlist you just created
    addTracks(playlist, uri1, headers)
    addTracks(playlist, uri2, headers)

