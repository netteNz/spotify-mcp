from .client import get_client


def _lean_track(track: dict) -> dict:
    return {
        "id": track.get("id"),
        "uri": track.get("uri"),
        "name": track.get("name"),
        "artist": ", ".join(a["name"] for a in track.get("artists", [])),
        "album": (track.get("album") or {}).get("name"),
        "duration_ms": track.get("duration_ms"),
        "popularity": track.get("popularity"),
    }


def get_saved_tracks(limit: int = 20, offset: int = 0) -> dict:
    """Get the current user's saved (Liked Songs) tracks as lean dicts."""
    sp = get_client()
    try:
        page = sp.current_user_saved_tracks(limit=limit, offset=offset)
        items = []
        for entry in page.get("items", []):
            track = entry.get("track") or {}
            lean = _lean_track(track)
            lean["added_at"] = entry.get("added_at")
            items.append(lean)
        return {
            "status": "success",
            "total": page.get("total"),
            "limit": page.get("limit"),
            "offset": page.get("offset"),
            "next": page.get("next") is not None,
            "items": items,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_playlists(limit: int = 20, offset: int = 0) -> dict:
    """Get the current user's playlists as lean dicts."""
    sp = get_client()
    try:
        page = sp.current_user_playlists(limit=limit, offset=offset)
        items = [
            {
                "id": p.get("id"),
                "uri": p.get("uri"),
                "name": p.get("name"),
                "owner": (p.get("owner") or {}).get("display_name"),
                "tracks_total": (p.get("tracks") or {}).get("total"),
                "public": p.get("public"),
                "collaborative": p.get("collaborative"),
            }
            for p in page.get("items", [])
        ]
        return {
            "status": "success",
            "total": page.get("total"),
            "limit": page.get("limit"),
            "offset": page.get("offset"),
            "next": page.get("next") is not None,
            "items": items,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_followed_artists(limit: int = 20) -> dict:
    """Get the current user's followed artists as lean dicts."""
    sp = get_client()
    try:
        page = sp.current_user_followed_artists(limit=limit)
        artists = (page or {}).get("artists", {})
        items = [
            {
                "id": a.get("id"),
                "uri": a.get("uri"),
                "name": a.get("name"),
                "genres": a.get("genres", []),
                "followers": (a.get("followers") or {}).get("total"),
                "popularity": a.get("popularity"),
            }
            for a in artists.get("items", [])
        ]
        return {
            "status": "success",
            "total": artists.get("total"),
            "limit": artists.get("limit"),
            "items": items,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def save_track(uri: str) -> dict:
    """Save a track to the user's library."""
    sp = get_client()
    try:
        track_id = uri.split(":")[-1] if "spotify:track:" in uri else uri
        sp.current_user_saved_tracks_add(tracks=[track_id])
        return {"status": "success", "action": "save_track", "uri": uri}
    except Exception as e:
        return {"status": "error", "message": str(e)}
