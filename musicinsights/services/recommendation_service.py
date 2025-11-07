from collections import Counter
from ..models import PlaylistEntry

def build_recommendations(upload):
    entries = PlaylistEntry.objects.filter(upload=upload).select_related('track')
    artist_counter = Counter()
    playlist_counter = Counter()
    time_of_day_counter = Counter()

    for e in entries:
        for artist in e.track.artists.all():
            artist_counter[artist.name] += 1
        if e.playlist_name:
            playlist_counter[e.playlist_name] += 1
        if e.added_at:
            time_of_day_counter[e.added_at.hour] += 1

    recs = []

    if artist_counter:
        top_artist, top_count = artist_counter.most_common(1)[0]
        if top_count >= 5:
            recs.append(f"You listen to {top_artist} quite a bit. It's worth putting together a playlist just for them with less obvious tracks.")

    morning_adds = sum(cnt for h, cnt in time_of_day_counter.items() if 5 <= h <= 10)
    if morning_adds >= 5:
        recs.append("You add a lot of music in the morning. Put together a 'morning focus' playlist with the songs you like best.")

    if playlist_counter:
        biggest_pl, count_pl = playlist_counter.most_common(1)[0]
        recs.append(f"Your most complete playlist is '{biggest_pl}'. Perhaps dividing it by theme will help you find music faster.")

    return recs
