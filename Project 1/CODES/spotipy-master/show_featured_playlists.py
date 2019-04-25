# shows artist info for a URN or URL

import spotipy
import sys
import pprint
import spotipy.util as util
import spotipy.oauth2 as oauth2

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python featured_playlists.py [username]")
    username="21hp6bjdej4iw3p7r7ku6k3hy"

token = util.prompt_for_user_token(username)
#print (token)
if token:
    sp = spotipy.Spotify(auth=token)

    response = sp.featured_playlists()
    print(response['message'])

    while response:
        playlists = response['playlists']
        for i, item in enumerate(playlists['items']):
            print(playlists['offset'] + i, item['name'])

        if playlists['next']:
            response = sp.next(playlists)
        else:
            response = None
else:
    print("Can't get token for", username)
