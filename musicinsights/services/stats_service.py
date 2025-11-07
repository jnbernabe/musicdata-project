from collections import Counter
from ..models import PlaylistEntry

def build_dashboard_context(upload):
    entries = PlaylistEntry.objects.filter(upload=upload).select_related('track', 'track__album')
    total_tracks = entries.count()

    artist_counter = Counter()
    track_counter = Counter()
    playlist_counter = Counter()
    monthly_counter = Counter()

    for e in entries:
        track = e.track
        for artist in track.artists.all():
            artist_counter[artist.name] += 1

        track_counter[track.name] += 1

        if e.playlist_name:
            playlist_counter[e.playlist_name] += 1

        if e.added_at:
            key = e.added_at.strftime('%Y-%m')
            monthly_counter[key] += 1

    monthly_labels = sorted(monthly_counter.keys())
    monthly_values = [monthly_counter[m] for m in monthly_labels]

    return {
        "total_tracks": total_tracks,
        "top_artists": artist_counter.most_common(10),
        "top_tracks": track_counter.most_common(10),
        "top_playlists": playlist_counter.most_common(10),
        "monthly_labels": monthly_labels,
        "monthly_values": monthly_values,
    }