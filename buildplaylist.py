import requests
import json

def getTopSongs(offset, token):

    url = "https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=50&offset=" + str(offset)

    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
    }

    r = requests.get(url, headers=headers, allow_redirects=False)

    uriList = []

    for i in r.json()['items']:
        uri = i['uri']
        uriList.append(uri)

    return uriList

def createPlaylist(name, token):

    createPlaylistUrl = "https://api.spotify.com/v1/me/playlists"

    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
    }

    playlistParams = {"name": name}

    try:
        print "Creating playlist named: " + name
        r = requests.post(createPlaylistUrl, headers=headers, allow_redirects=False, data=json.dumps(playlistParams))
        playlistId = r.json()['id']
        print "Success! Created playlist with ID " + playlistId

    except:
        print "Failed with status code: " + r.status_code

    return playlistId

def addTracks(playlistId, uris, token):
        
    addTracksUrl = "https://api.spotify.com/v1/playlists/" + playlistId + "/tracks"

    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
    }

    trackParams = {"uris": uris}

    try:
        print "Adding tracks to playlist..."
        r = requests.post(addTracksUrl, headers=headers, allow_redirects=False, data=json.dumps(trackParams))
        print "Success! Added " + str(len(uris)) + " tracks to playlist " + playlistId

    except:
        print "Failed with status code: " + r.status_code

    return

if __name__ == "__main__":

    token = ""

    # Create playlist
    playlistName = "Your Top Songs of the Decade"
    playlist = createPlaylist(playlistName, token)

    # Get your top 100 songs
    uri1 = getTopSongs(0, token)
    uri2 = getTopSongs(49, token)

    # Add the tracks to the playlist you just created
    addTracks(playlist, uri1, token)
    addTracks(playlist, uri2, token)

