from django.db import models

# Create your models here.
from django.db.models import ImageField, FileField, ForeignKey, TextField


class Background(models.Model):
    display_name = TextField()
    image = ImageField()
    link = TextField(default='')

    def __str__(self):
        return self.display_name


class Song(models.Model):
    display_name = TextField()
    mpeg_file = FileField()
    ogg_file = FileField()

    def __str__(self):
        return self.display_name


class Encounter(models.Model):
    background = ForeignKey(Background, on_delete=models.CASCADE)
    song = ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.background.display_name
