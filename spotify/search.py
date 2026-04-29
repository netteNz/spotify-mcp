from .client import get_client
from . import playback


def _lean_track(t: dict) -> dict:
    return {
        "id": t.get("id"),
        "uri": t.get("uri"),
        "name": t.get("name"),
        "artist": ", ".join(a["name"] for a in t.get("artists", [])),
        "album": (t.get("album") or {}).get("name"),
        "duration_ms": t.get("duration_ms"),
        "popularity": t.get("popularity"),
    }


def _lean_artist(a: dict) -> dict:
    return {
        "id": a.get("id"),
        "uri": a.get("uri"),
        "name": a.get("name"),
        "genres": a.get("genres", []),
        "followers": (a.get("followers") or {}).get("total"),
        "popularity": a.get("popularity"),
    }


def _lean_album(al: dict) -> dict:
    return {
        "id": al.get("id"),
        "uri": al.get("uri"),
        "name": al.get("name"),
        "artist": ", ".join(a["name"] for a in al.get("artists", [])),
        "release_date": al.get("release_date"),
        "total_tracks": al.get("total_tracks"),
    }


def search(q: str, type: str = "track,artist,album", limit: int = 20) -> dict:
    """
    Generic Spotify search. `type` can be a comma-separated list of:
    track, artist, album, playlist. Returns lean items per requested type.
    """
    sp = get_client()
    try:
        raw = sp.search(q=q, limit=limit, type=type)
        out: dict = {"status": "success", "query": q}
        if "tracks" in raw:
            out["tracks"] = [_lean_track(t) for t in raw["tracks"].get("items", [])]
        if "artists" in raw:
            out["artists"] = [_lean_artist(a) for a in raw["artists"].get("items", [])]
        if "albums" in raw:
            out["albums"] = [_lean_album(al) for al in raw["albums"].get("items", [])]
        if "playlists" in raw:
            out["playlists"] = [
                {
                    "id": p.get("id"),
                    "uri": p.get("uri"),
                    "name": p.get("name"),
                    "owner": (p.get("owner") or {}).get("display_name"),
                    "tracks_total": (p.get("tracks") or {}).get("total"),
                }
                for p in raw["playlists"].get("items", [])
            ]
        return out
    except Exception as e:
        return {"status": "error", "message": str(e)}


def search_track(query: str, limit: int = 10) -> dict:
    """Search Spotify for tracks. Returns lean track dicts."""
    sp = get_client()
    try:
        raw = sp.search(q=query, type="track", limit=limit)
        items = [_lean_track(t) for t in raw.get("tracks", {}).get("items", [])]
        return {"status": "success", "query": query, "count": len(items), "items": items}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def search_artist(query: str, limit: int = 10) -> dict:
    """Search Spotify for artists. Returns lean artist dicts."""
    sp = get_client()
    try:
        raw = sp.search(q=query, type="artist", limit=limit)
        items = [_lean_artist(a) for a in raw.get("artists", {}).get("items", [])]
        return {"status": "success", "query": query, "count": len(items), "items": items}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def search_and_play(query: str, device_id: str = None) -> dict:
    """
    Search for a track by query string and immediately play the top result
    on the active or specified device.
    """
    sp = get_client()
    try:
        raw = sp.search(q=query, type="track", limit=1)
        items = raw.get("tracks", {}).get("items", [])
        if not items:
            return {"status": "error", "message": f"No track found for query: {query}"}
        track = _lean_track(items[0])
        result = playback.play(uri=track["uri"], device_id=device_id)
        return {"status": result.get("status", "success"), "track": track, "playback": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
