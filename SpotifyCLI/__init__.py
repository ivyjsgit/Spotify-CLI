import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import spotipy.client as client
import configparser

''' shows the albums and tracks for a given artist.
'''


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def get_album_uri(name):
	albums = []
	uris = []
	results = sp.search(q=name, limit=10, type='album')
#     print(results)
	items = results['albums'].get('items')

	for count in range(0, len(items)):
		uris.append(items[count]['uri'])
		artist = results['albums'].get('items')[count].get('artists')[0].get('name')
		print('('+str(count)+') '+items[count]['name'] + ": " + artist)

	selection = int(input("Selection: "))
	# print(uris[selection])
	selectedURI = uris[selection]
	sp.start_playback(context_uri=get_uri_from_album(selectedURI))


def show_artist_albums(artist):
	albums = []
	uris = []
	results = sp.artist_albums(artist['id'], album_type='album')
	# print(results['items'])
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


def get_uri_from_track(track_uri):
	ourTrack = sp.track(track_uri)
	# print(ourTrack.get('uri'))
	# sp.start_playback(context_uri=ourTrack.get('uri'))
	return (ourTrack.get('uri'))
	
def show_arist_songs(artist):
	songs = []
	uris = []
	results = sp.artist_top_tracks(artist['id'])
	# print(results)
	# print(results['tracks'][1]['name'])
	
	for count in range(1, 10):
		songs.append(results['tracks'][count]['name'])
		uris.append(results['tracks'][count]['uri'])
	count = 0
	for song in songs:
		print('(' + str(count) + ') ' + song )
		count +=1
	selection = int(input("Selection: "))
	selectedURI = uris[selection]
	ourID = get_uri_from_track(selectedURI)
	sp.start_playback(uris=[ourID])

def search_songs(query):
	songs = []
	uris = []
	artists = []
	results = sp.search(query, limit=10)
	for count in range(0, len(results['tracks']['items'])):
		artists.append(results['tracks']['items'][count]['artists'][0]['name'])
		songs.append(results['tracks']['items'][count]['name'])
		uris.append(results['tracks']['items'][count]['uri'])
	count = 0
	# print(artists)
	for song in songs:
		print('(' + str(count) + ') ' + song + ": " + artists[count])
		count += 1
	selection = int(input("Selection: "))
	selectedURI = uris[selection]
	# print(selectedURI)
	ourID = get_uri_from_track(selectedURI)
	sp.start_playback(uris=[ourID])

config = configparser.ConfigParser()
config.read('config.ini')
ourClientID = config['KEYS']['client_id']
ourSecret = config['KEYS']['client_secret']
ourUsername = config['KEYS']['username']
scope = 'user-modify-playback-state user-read-playback-state'
token = util.prompt_for_user_token(ourUsername, scope, client_id=ourClientID,
							client_secret=ourSecret, redirect_uri='http://localhost/')

sp = spotipy.Spotify(auth=token)
if len(sys.argv) < 2:
	print(('Usage: {0} artist name'.format(sys.argv[0])))
else:
	if(sys.argv[1]) == '-aa':
		name = ' '.join(sys.argv[2:])
		artist = get_artist(name)
		if artist:
			show_artist_albums(artist)
		else:
			print("Can't find that artist")
	elif (sys.argv[1]) == '-album':
		name = ' '.join(sys.argv[2:])
		# print(name)
		albums = get_album_uri(name)
		# print(albums)

	elif (sys.argv[1]) == '-ff':
		sp.next_track()
	elif (sys.argv[1]) == '-b':
		sp.previous_track()
	elif (sys.argv[1]) == '-p':
		if (sp.current_playback()['is_playing']):
			sp.pause_playback()
		else:
			sp.start_playback()
	elif (sys.argv[1]) == '-artist':
		name = ' '.join(sys.argv[2:])
		artist = get_artist(name)
		# print(artist)
		# artist = 'spotify:artist:1R84VlXnFFULOsWWV8IrCQ'
		show_arist_songs(artist)
	elif (sys.argv[1]) == '-song':
		name = ' '.join(sys.argv[2:])
		search_songs(name)
