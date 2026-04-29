from .client import get_client

def get_audio_features(track_uris: list[str]) -> dict:
    """Get audio features (danceability, energy, etc.) for a list of tracks."""
    sp = get_client()
    try:
        ids = [uri.split(":")[-1] if "spotify:track:" in uri else uri for uri in track_uris]
        features = sp.audio_features(tracks=ids)
        return {"status": "success", "features": features}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_top_tracks(limit: int = 20, time_range: str = 'medium_term') -> dict:
    """
    Get the user's top tracks.
    time_range options: 'short_term', 'medium_term', 'long_term'
    """
    sp = get_client()
    try:
        if time_range not in ['short_term', 'medium_term', 'long_term']:
            time_range = 'medium_term'
        return sp.current_user_top_tracks(limit=limit, time_range=time_range)
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_recommendations(seed_artists: list[str] = None, seed_genres: list[str] = None, seed_tracks: list[str] = None, limit: int = 20) -> dict:
    """Get recommendations based on seed artists, genres, or tracks."""
    sp = get_client()
    try:
        clean_artists = [uri.split(":")[-1] if "spotify:artist:" in uri else uri for uri in seed_artists] if seed_artists else None
        clean_tracks = [uri.split(":")[-1] if "spotify:track:" in uri else uri for uri in seed_tracks] if seed_tracks else None
        
        return sp.recommendations(
            seed_artists=clean_artists,
            seed_genres=seed_genres,
            seed_tracks=clean_tracks,
            limit=limit
        )
    except Exception as e:
        return {"status": "error", "message": str(e)}
