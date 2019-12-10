# spotify-top-songs

I was hoping [Spotify's "Best of the Decade For You" playlist](https://www.cnet.com/how-to/spotify-wrapped-how-to-see-your-top-songs-for-2019-and-the-decade/)
would list my most played tracks this decade (or however long I've been using
Spotify), but unfortunately that wasn't the case since it listed songs I definitely did not recognize.

As an alternative, I looked into ways to get this track list from the [Spotify Web API](https://developer.spotify.com/documentation/web-api/), and found [this handy piece of documentation](https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/).

If you'd like to run this script yourself, you need an OAuth token:
1. Go to [this page](https://developer.spotify.com/documentation/web-api/reference/personalization/get-users-top-artists-and-tracks/).
2. Click "Try it" under the ***Examples*** section.
3. Log into your Spotify account, if prompted.

Once you've entered your Spotify credentials, you should see your OAuth token
under the "OAuth Token" field.  Paste this token into the `token` variable in
the `get-top-songs.py` script and run the script to get your 100 most popular
songs on Spotify!

### Next steps:

- Modify the script to actually create the playlist for you given the list of songs generated.

