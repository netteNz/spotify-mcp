import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

_client: spotipy.Spotify | None = None

SCOPES = [
    "user-read-playback-state",
    "user-modify-playback-state",
    "user-read-currently-playing",
    "user-library-read",
    "user-top-read",
    "user-read-recently-played",
    "playlist-read-private",
    "playlist-modify-private",
    "playlist-modify-public",
]

def get_client() -> spotipy.Spotify:
    global _client
    if _client is None:
        _client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                scope=" ".join(SCOPES),
                cache_path=".spotify_cache",   # persists token to disk
                open_browser=True,
            )
        )
    return _client
