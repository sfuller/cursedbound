from django.contrib import admin
from django.contrib.admin import register

from cursedboundapp.models import Background, Song, Encounter


@register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('display_name',)


@register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('display_name',)


@register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('display_name',)

    def display_name(self, obj: Encounter):
        return obj.background.display_name
