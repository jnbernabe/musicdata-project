from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from musicinsights.models import Upload, Artist, Album, Track, PlaylistEntry
from musicinsights.services.exportify_parser import parse_exportify_file

class ExportifyParserTest(TestCase):
    def test_parse_valid_csv(self):
        csv_content = (
            "Track URI,Track Name,Album Name,Artist Name(s),Added At,Duration (ms),Genres,Danceability,Energy,Valence\n"
            "spotify:track:1,Song A,Album A,Artist A,2023-01-01T12:00:00Z,1000,Pop,0.5,0.8,0.9\n"
            "spotify:track:2,Song B,Album B,Artist B,2023-01-02T12:00:00Z,2000,Rock,0.6,0.7,0.4"
        ).encode('utf-8')
        
        file = SimpleUploadedFile("test_playlist.csv", csv_content, content_type="text/csv")
        upload = Upload.objects.create(original_file=file)
        
        parse_exportify_file(upload)
        
        self.assertEqual(Artist.objects.count(), 2)
        self.assertEqual(Album.objects.count(), 2)
        self.assertEqual(Track.objects.count(), 2)
        self.assertEqual(PlaylistEntry.objects.count(), 2)
        
        track_a = Track.objects.get(name="Song A")
        self.assertEqual(track_a.album.name, "Album A")
        self.assertTrue(track_a.artists.filter(name="Artist A").exists())
        self.assertEqual(track_a.danceability, 0.5)
        self.assertEqual(track_a.energy, 0.8)

    def test_parse_invalid_file_extension(self):
        file = SimpleUploadedFile("test.txt", b"content", content_type="text/plain")
        upload = Upload.objects.create(original_file=file)
        
        with self.assertRaises(ValueError):
            parse_exportify_file(upload)
