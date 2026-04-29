from mcp.server.fastmcp import FastMCP
from spotify import playback, library, analytics, search

# Initialize FastMCP server
mcp = FastMCP("Spotify")

# --- Playback Tools ---

@mcp.tool()
def play(uri: str = None, device_id: str = None) -> str:
    """
    Play a track, album, artist, or playlist.
    If no URI is provided, resumes current playback.
    """
    return playback.play(uri, device_id)

@mcp.tool()
def pause(device_id: str = None) -> str:
    """Pause playback on the active device."""
    return playback.pause(device_id)

@mcp.tool()
def skip_next(device_id: str = None) -> str:
    """Skip to the next track."""
    return playback.skip_to_next(device_id)

@mcp.tool()
def skip_previous(device_id: str = None) -> str:
    """Skip to the previous track."""
    return playback.skip_to_previous(device_id)

@mcp.tool()
def set_volume(volume_percent: int, device_id: str = None) -> str:
    """Set the volume (0-100)."""
    return playback.set_volume(volume_percent, device_id)

@mcp.tool()
def get_devices() -> dict:
    """Get available playback devices."""
    return playback.get_devices()

@mcp.tool()
def get_currently_playing() -> dict:
    """Get the currently playing track and state."""
    return playback.get_currently_playing()

# --- Library Tools ---

@mcp.tool()
def get_saved_tracks(limit: int = 20, offset: int = 0) -> dict:
    """Get the current user's saved tracks."""
    return library.get_saved_tracks(limit, offset)

@mcp.tool()
def get_playlists(limit: int = 20, offset: int = 0) -> dict:
    """Get the current user's playlists."""
    return library.get_playlists(limit, offset)

@mcp.tool()
def get_followed_artists(limit: int = 20) -> dict:
    """Get the current user's followed artists."""
    return library.get_followed_artists(limit)

@mcp.tool()
def save_track(uri: str) -> str:
    """Save a track to the user's library."""
    return library.save_track(uri)

# --- Analytics Tools ---

@mcp.tool()
def get_audio_features(track_uris: list[str]) -> list:
    """Get audio features (danceability, energy, etc.) for a list of tracks."""
    return analytics.get_audio_features(track_uris)

@mcp.tool()
def get_top_tracks(limit: int = 20, time_range: str = 'medium_term') -> dict:
    """
    Get the user's top tracks.
    time_range options: 'short_term', 'medium_term', 'long_term'
    """
    return analytics.get_top_tracks(limit, time_range)

@mcp.tool()
def get_recommendations(seed_artists: list[str] = None, seed_genres: list[str] = None, seed_tracks: list[str] = None, limit: int = 20) -> dict:
    """Get recommendations based on seed artists, genres, or tracks."""
    return analytics.get_recommendations(seed_artists, seed_genres, seed_tracks, limit)

# --- Search Tools ---

@mcp.tool()
def search_spotify(q: str, type: str = 'track,artist,album', limit: int = 20) -> dict:
    """
    Search for tracks, artists, or albums on Spotify.
    `type` can be a comma-separated list of: track, artist, album, playlist
    """
    return search.search(q, type, limit)

if __name__ == "__main__":
    mcp.run()
