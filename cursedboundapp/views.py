import random
from typing import Optional, Tuple

from django.http import HttpRequest
from django.shortcuts import render

from cursedboundapp.models import Encounter


SESSION_KEY_ENCOUNTER_INDEX = 'encounter_index'
SESSION_KEY_ENCOUNTERS = 'encounters'


def encounter(request: HttpRequest) -> None:

    encounters = request.session.get(SESSION_KEY_ENCOUNTERS)
    encounter_index = int(request.session.get(SESSION_KEY_ENCOUNTER_INDEX, 0))
    all_encounters: Optional[Tuple[Encounter]] = None

    if encounters is None:
        all_encounters = tuple(Encounter.objects.all())
        encounter_count = len(all_encounters)
        encounters = list(range(encounter_count))
        random.shuffle(encounters)
        request.session[SESSION_KEY_ENCOUNTERS] = encounters
        encounter_index = 0

    if all_encounters is None:
        all_encounters = tuple(Encounter.objects.all())

    encounter: Encounter = all_encounters[encounters[encounter_index]]
    encounter_index += 1
    request.session[SESSION_KEY_ENCOUNTER_INDEX] = encounter_index

    if encounter_index >= len(encounters):
        request.session[SESSION_KEY_ENCOUNTERS] = None

    context = {
        'background_url': encounter.background.image.url,
        'song_mpeg_url': encounter.song.mpeg_file.url,
        'song_ogg_url': encounter.song.ogg_file.url
    }

    return render(request, 'encounter.html', context)
