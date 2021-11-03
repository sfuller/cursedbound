import random
from typing import Optional, Tuple

import django.conf
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from cursedboundapp.models import Encounter, Game

SESSION_KEY_ENCOUNTER_INDEX = 'encounter_index'
SESSION_KEY_ENCOUNTERS = 'encounters'


def encounter(request) -> HttpResponse:
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

    return render_encounter(request, encounter)


def specific_encounter(request: HttpRequest, *, id: str) -> HttpResponse:
    def do_redirect():
        return redirect('random')

    try:
        int_id = int(id)
    except (ValueError, TypeError):
        return do_redirect()

    try:
        encounter = Encounter.objects.get(pk=id)
    except Encounter.DoesNotExist:
        return redirect('random')

    return render_encounter(request, encounter)


STATUS_BAR_FILES = {
    Game.EARTHBOUND: 'status.png',
    Game.MOTHER: 'mother_status.png',
    Game.MOTHER3: 'mother3_status.png'
}


def render_encounter(request: HttpRequest, encounter: Encounter) -> HttpResponse:

    context = {
        'image_link': encounter.background.link,
        'image_id': encounter.pk,
        'suggestions_link': django.conf.settings.CURSEDBOUND_SUGGESTIONS_URL,
        'background_url': encounter.background.image.url,
        'song_mpeg_url': encounter.song.mpeg_file.url,
        'song_ogg_url': encounter.song.ogg_file.url,
        'statusbar_file': STATUS_BAR_FILES[Game(encounter.song.game)]
    }

    return render(request, 'encounter.html', context)
