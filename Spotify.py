import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import spotipy.client as client


''' shows the albums and tracks for a given artist.
'''


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_artist_albums(artist):
	albums = []
	uris = []
	results = sp.artist_albums(artist['id'], album_type='album')
	albums.extend(results['items'])
	while results['next']:
		results = sp.next(results)
		albums.extend(results['items'])
	seen = set()  # to avoid dups
	albums.sort(key=lambda album: album['name'].lower())
	count = 0
	for album in albums:
		name = album['name']
		if name not in seen:
			print(('(' + str(count) + ') ' + name))
			uris.append(album['uri'])
			count +=1
		# for k, v in album.items():
		# 	  print(k,v)
		seen.add(name)
	# print(uris)
	selection = int(input("Selection: "))
	# print(uris[selection])
	selectedURI = uris[selection]
	sp.start_playback(context_uri=get_uri_from_album(selectedURI))

def get_uri_from_album(albumuri):
	ourAlbum = sp.album(albumuri)
	# sp.start_playback(context_uri=ourAlbum.get('uri'))
	return(ourAlbum.get('uri'))

scope = 'user-modify-playback-state'
username = ''
client_id = ''
client_secret = ''
token = util.prompt_for_user_token(username, scope, client_id=client_id,
                                   client_secret=client_secret, redirect_uri='http://localhost/')

sp = spotipy.Spotify(auth=token)

ourAlbum = sp.album('spotify:album:04EajKw866bzJn3EW8HOdQ')
album_name = ourAlbum.get('name')
# sp.start_playback(context_uri=ourAlbum.get('uri'))
print(ourAlbum.get('uri'))
print(album_name)

# sp.start_playback(uris='spotify:album:04EajKw866bzJn3EW8HOdQ')

if len(sys.argv) < 2:
	print(('Usage: {0} artist name'.format(sys.argv[0])))
else:
	if(sys.argv[1]) == '-a':
		name = ' '.join(sys.argv[2:])
		artist = get_artist(name)
		if artist:
			show_artist_albums(artist)
		else:
			print("Can't find that artist")
	elif (sys.argv[1]) == '-ff':
		sp.next_track()
	elif (sys.argv[1]) == '-b':
		sp.previous_track()
