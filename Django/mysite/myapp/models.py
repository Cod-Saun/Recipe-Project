from django.db import models

# Create your models here.
class Playlist(models.Model):
    Song_Name = models.CharField(max_length=40)
    Artist_Name = models.CharField(max_length=30)
    Album_Name = models.CharField(max_length=30)
    Song_Duration = models.CharField(max_length=5)

    def __str__(self):
        return self.Song_Name
