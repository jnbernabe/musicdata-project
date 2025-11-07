from django.db import models

# Create your models here.

class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    original_file = models.FileField(upload_to='uploads/')


    def __str__(self):
        return f"Upload {self.id} at {self.created_at}"

class Artist(models.Model):
    spotify_id = models.CharField(max_length =100, unique= True)
    name = models.CharField (max_length=255)

    def __str__(self):
        return self.name

class Album(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
    
class Track(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    duration_ms = models.IntegerField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    artists = models.ManyToManyField(Artist, related_name='tracks')
    genres = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    
class PlaylistEntry(models.Model):
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='entries')
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=255, blank=True, null=True)
    added_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-added_at']