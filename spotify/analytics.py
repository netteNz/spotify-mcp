from .client import get_client

_AUDIO_FEATURE_FIELDS = (
    "id",
    "tempo",
    "key",
    "mode",
    "energy",
    "valence",
    "danceability",
    "instrumentalness",
)


def _to_id(uri_or_id: str) -> str:
    return uri_or_id.split(":")[-1] if ":" in uri_or_id else uri_or_id


def get_audio_features(track_ids: list[str]) -> dict:
    """
    Get audio features for a list of track URIs or IDs.

    Batches requests in groups of 100 (Spotify API limit) and returns a lean
    shape per track: id, tempo, key, mode, energy, valence, danceability,
    instrumentalness.
    """
    sp = get_client()
    try:
        if not track_ids:
            return {"status": "success", "features": []}

        ids = [_to_id(t) for t in track_ids if t]
        features: list[dict] = []
        for i in range(0, len(ids), 100):
            chunk = ids[i : i + 100]
            batch = sp.audio_features(tracks=chunk) or []
            for f in batch:
                if not f:
                    continue
                features.append({k: f.get(k) for k in _AUDIO_FEATURE_FIELDS})
        return {"status": "success", "count": len(features), "features": features}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_top_tracks(limit: int = 20, time_range: str = "medium_term") -> dict:
    """
    Get the user's top tracks as lean dicts.
    time_range options: 'short_term', 'medium_term', 'long_term'.
    """
    sp = get_client()
    try:
        if time_range not in ("short_term", "medium_term", "long_term"):
            time_range = "medium_term"
        page = sp.current_user_top_tracks(limit=limit, time_range=time_range)
        items = [
            {
                "id": t.get("id"),
                "uri": t.get("uri"),
                "name": t.get("name"),
                "artist": ", ".join(a["name"] for a in t.get("artists", [])),
                "album": (t.get("album") or {}).get("name"),
                "popularity": t.get("popularity"),
                "duration_ms": t.get("duration_ms"),
            }
            for t in page.get("items", [])
        ]
        return {
            "status": "success",
            "time_range": time_range,
            "total": page.get("total"),
            "items": items,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


def get_recommendations(
    seed_artists: list[str] = None,
    seed_genres: list[str] = None,
    seed_tracks: list[str] = None,
    limit: int = 20,
) -> dict:
    """Get recommendations based on seed artists, genres, or tracks."""
    sp = get_client()
    try:
        clean_artists = [_to_id(u) for u in seed_artists] if seed_artists else None
        clean_tracks = [_to_id(u) for u in seed_tracks] if seed_tracks else None

        result = sp.recommendations(
            seed_artists=clean_artists,
            seed_genres=seed_genres,
            seed_tracks=clean_tracks,
            limit=limit,
        )
        items = [
            {
                "id": t.get("id"),
                "uri": t.get("uri"),
                "name": t.get("name"),
                "artist": ", ".join(a["name"] for a in t.get("artists", [])),
                "album": (t.get("album") or {}).get("name"),
                "popularity": t.get("popularity"),
                "duration_ms": t.get("duration_ms"),
            }
            for t in result.get("tracks", [])
        ]
        return {"status": "success", "count": len(items), "items": items}
    except Exception as e:
        return {"status": "error", "message": str(e)}
