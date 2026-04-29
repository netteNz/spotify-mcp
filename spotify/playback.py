from .client import get_client

def play(uri: str = None, device_id: str = None) -> dict:
    """
    Play a track, album, artist, or playlist.
    If no URI is provided, resumes current playback.
    """
    sp = get_client()
    
    try:
        if uri:
            if "spotify:track:" in uri:
                sp.start_playback(device_id=device_id, uris=[uri])
                return {"status": "success", "action": "play", "type": "track", "uri": uri}
            elif any(x in uri for x in ["spotify:album:", "spotify:playlist:", "spotify:artist:"]):
                sp.start_playback(device_id=device_id, context_uri=uri)
                return {"status": "success", "action": "play", "type": "context", "uri": uri}
            else:
                if ":" not in uri:
                    track_uri = f"spotify:track:{uri}"
                    sp.start_playback(device_id=device_id, uris=[track_uri])
                    return {"status": "success", "action": "play", "type": "track", "uri": track_uri}
                else:
                    return {"status": "error", "message": f"Invalid URI format: {uri}"}
        else:
            sp.start_playback(device_id=device_id)
            return {"status": "success", "action": "resume"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def pause(device_id: str = None) -> dict:
    """Pause playback."""
    sp = get_client()
    try:
        sp.pause_playback(device_id=device_id)
        return {"status": "success", "action": "pause"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def skip_to_next(device_id: str = None) -> dict:
    """Skip to the next track."""
    sp = get_client()
    try:
        sp.next_track(device_id=device_id)
        return {"status": "success", "action": "skip_next"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def skip_to_previous(device_id: str = None) -> dict:
    """Skip to the previous track."""
    sp = get_client()
    try:
        sp.previous_track(device_id=device_id)
        return {"status": "success", "action": "skip_previous"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def set_volume(volume_percent: int, device_id: str = None) -> dict:
    """Set the volume (0-100)."""
    sp = get_client()
    try:
        if not 0 <= volume_percent <= 100:
            return {"status": "error", "message": "Volume must be between 0 and 100"}
        sp.volume(volume_percent, device_id=device_id)
        return {"status": "success", "action": "set_volume", "volume_percent": volume_percent}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_devices() -> dict:
    """Get available playback devices."""
    sp = get_client()
    try:
        return sp.devices()
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_currently_playing() -> dict:
    """Get the currently playing track and state."""
    sp = get_client()
    try:
        current = sp.currently_playing()
        if current is None:
            return {"status": "inactive", "message": "No active playback session found."}
        return current
    except Exception as e:
        return {"status": "error", "message": str(e)}
