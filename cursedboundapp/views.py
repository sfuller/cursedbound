import random
from typing import Optional

from django.http import HttpRequest
from django.shortcuts import render

from cursedboundapp.models import Encounter


SESSION_KEY_LAST_ENCOUNTER_INDEX = 'last_encounter_index'


def encounter(request: HttpRequest) -> None:

    last_encounter: Optional[int] = request.session.get(SESSION_KEY_LAST_ENCOUNTER_INDEX)

    all_encounters = tuple(Encounter.objects.all())
    encounter_count = len(all_encounters)
    index = random.randrange(0, encounter_count)

    if last_encounter is not None and index == last_encounter:
        index = (index + 1) % encounter_count

    request.session[SESSION_KEY_LAST_ENCOUNTER_INDEX] = index

    encounter: Encounter = all_encounters[index]

    context = {
        'background_url': encounter.background.image.url,
        'song_mpeg_url': encounter.song.mpeg_file.url,
        'song_ogg_url': encounter.song.ogg_file.url
    }

    return render(request, 'encounter.html', context)
