from .client import get_client

def get_saved_tracks(limit: int = 20, offset: int = 0) -> dict:
    """Get the current user's saved tracks."""
    sp = get_client()
    try:
        return sp.current_user_saved_tracks(limit=limit, offset=offset)
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_playlists(limit: int = 20, offset: int = 0) -> dict:
    """Get the current user's playlists."""
    sp = get_client()
    try:
        return sp.current_user_playlists(limit=limit, offset=offset)
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_followed_artists(limit: int = 20) -> dict:
    """Get the current user's followed artists."""
    sp = get_client()
    try:
        return sp.current_user_followed_artists(limit=limit)
    except Exception as e:
        return {"status": "error", "message": str(e)}

def save_track(uri: str) -> dict:
    """Save a track to the user's library."""
    sp = get_client()
    try:
        if "spotify:track:" in uri:
            track_id = uri.split(":")[-1]
        else:
            track_id = uri
            
        sp.current_user_saved_tracks_add(tracks=[track_id])
        return {"status": "success", "action": "save_track", "uri": uri}
    except Exception as e:
        return {"status": "error", "message": str(e)}
