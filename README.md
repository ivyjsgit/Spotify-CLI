# Installation

Run ```pip install -r requirements.txt``` and ```pip install -e .``` in order to install the project.

You can run ```pip install SpotifyCLI```, but in my experience, this appears outdated for some reason, even though it shows the correct version on PyPi. 

Be sure export SpotifyClientID, SpotifyClientSecret, and SpotifyUsername. to ~/.zshrc or ~/.bashrc. SpotifyUsername is NOT your email, but it is the random string of numbers and digits that appear when you view your profile on Spotify.

# Getting an API key

Head [here](https://developer.spotify.com) to get a key. Set the Callback URL to http://localhost


# Commands: 
-album: Searches for albumname

-aa: Pull up albums by a given artist

-ff: Skip song

-b: Back

-o: Toggle music playback

-artist: Pull up top songs by artist

-song: Pull up song with name
