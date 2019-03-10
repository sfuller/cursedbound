import enum

from django.db import models

# Create your models here.
from django.db.models import ImageField, FileField, ForeignKey, TextField, IntegerField


class Game(enum.Enum):
    EARTHBOUND = 0
    MOTHER = 1
    MOTHER3 = 2


class Background(models.Model):
    display_name = TextField()
    image = ImageField()
    link = TextField(default='', blank=True)

    def __str__(self):
        return self.display_name


class Song(models.Model):
    display_name = TextField()
    mpeg_file = FileField()
    ogg_file = FileField()
    game = IntegerField(choices=[(e.value, str(e)) for e in Game], default=Game.EARTHBOUND.value)

    def __str__(self):
        return self.display_name


class Encounter(models.Model):
    background = ForeignKey(Background, on_delete=models.CASCADE)
    song = ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.background.display_name
