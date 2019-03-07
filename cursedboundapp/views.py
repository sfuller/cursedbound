import random
from django.http import HttpRequest
from django.shortcuts import render

from cursedboundapp.models import Encounter


def encounter(request: HttpRequest) -> None:

    all_encounters = tuple(Encounter.objects.all())
    index = random.randrange(0, len(all_encounters))
    encounter: Encounter = all_encounters[index]

    context = {
        'background_url': encounter.background.image.url,
        'song_mpeg_url': encounter.song.mpeg_file.url,
        'song_ogg_url': encounter.song.ogg_file.url
    }

    return render(request, 'encounter.html', context)
