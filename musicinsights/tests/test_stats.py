from django.test import TestCase
from musicinsights.models import Upload, Artist, Album, Track, PlaylistEntry
from musicinsights.services.stats_service import build_dashboard_context
from datetime import datetime

class StatsServiceTest(TestCase):
    def setUp(self):
        self.upload = Upload.objects.create()
        self.artist = Artist.objects.create(name="Artist A", spotify_id="a1")
        self.album = Album.objects.create(name="Album A", spotify_id="al1")
        self.track = Track.objects.create(name="Song A", spotify_id="t1", album=self.album)
        self.track.artists.add(self.artist)
        
        PlaylistEntry.objects.create(
            upload=self.upload,
            track=self.track,
            playlist_name="My Playlist",
            added_at=datetime(2023, 1, 1)
        )

    def test_build_dashboard_context(self):
        context = build_dashboard_context(self.upload)
        
        self.assertEqual(context['total_tracks'], 1)
        self.assertIn('total_listening_hours', context)
        self.assertEqual(context['top_artists'][0][0], "Artist A")
        self.assertEqual(context['top_tracks'][0]['name'], "Song A")
        self.assertEqual(context['top_tracks'][0]['artist'], "Artist A")
        self.assertIn('listening_time_hours', context['top_tracks'][0])
        self.assertIn('avg_features', context)
        self.assertIn('top_genres', context)
