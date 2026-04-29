from .client import get_client

def search(q: str, type: str = 'track,artist,album', limit: int = 20) -> dict:
    """
    Search for tracks, artists, or albums.
    `type` can be a comma-separated list of: track, artist, album, playlist
    """
    sp = get_client()

    try:
        return sp.search(q=q, limit=limit, type=type)
    except Exception as e:
        return {"status": "error", "message": str(e)}
