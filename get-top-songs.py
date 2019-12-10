import requests
import json

def topSongs(offset):

    url = "https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=50&offset=" + str(offset)
    token = "your-token-here"
    headers = {
        'authorization': "Bearer " + token,
        'content-type': "application/json",
    }

    r = requests.get(url, headers=headers, allow_redirects=False)

    l = []
    for i in r.json()['items']:
        songName = i['name']
        artistName = i['artists'][0]['name']
        l.append(songName + " - " + artistName)
    return l

if __name__ == "__main__":

    print "Top 100 songs:\n--------------"
    l = topSongs(0) + topSongs(49)
    for num, el in enumerate(l):
        print str(num + 1) + ". " + el

