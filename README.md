# spotify-top-songs

I was hoping [Spotify's "Best of the Decade For You"
playlist](https://www.cnet.com/how-to/spotify-wrapped-how-to-see-your-top-songs-for-2019-and-the-decade/)
would list my most played tracks this decade (or however long I've been using
Spotify), but unfortunately that wasn't the case since the playlist listed
songs I definitely did not recognize.

As an alternative, I looked into ways to create it myself using the [Spotify
Web API](https://developer.spotify.com/documentation/web-api/), and found
[some](https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks)
[useful](https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/)
[documentation](https://developer.spotify.com/documentation/web-api/reference/playlists/create-playlist/).

If you'd like to run this script yourself, you need a Spotify OAuth token.
Here's a way to obtain one through the Spotify Web API docs:
1. Go to [this page](https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/).
2. Click "Try it" under the ***Examples*** section.

<img src="/img/tryit.png" width="500">

3. Log into your Spotify account, if prompted.

Once you've entered your Spotify credentials, you should see your OAuth token
under the "OAuth Token" field:

<img src="/img/oauth.png" width="500">

Paste this token into the `token` variable in the `buildplaylist.py` script and
run the script.  Restart your Spotify app and you should see your new playlist
containing your 100 most popular songs on Spotify!

