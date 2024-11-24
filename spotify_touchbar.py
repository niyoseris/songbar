import rumps
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-read-currently-playing'

class SpotifyTouchBarApp(rumps.App):
    def __init__(self):
        super(SpotifyTouchBarApp, self).__init__("Spotify TouchBar")
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        ))
        self.timer = rumps.Timer(self.update_song, 1)
        self.timer.start()

    def update_song(self, _):
        try:
            current_track = self.sp.current_user_playing_track()
            if current_track is not None and current_track['is_playing']:
                song_name = current_track['item']['name']
                artist_name = current_track['item']['artists'][0]['name']
                self.title = f"{song_name} - {artist_name}"
            else:
                self.title = "Not Playing"
        except Exception as e:
            self.title = "Error"
            print(f"Error: {e}")

if __name__ == '__main__':
    SpotifyTouchBarApp().run()
