import io

from django.contrib import admin
from django.contrib.admin import register
from django.urls import reverse
from pydub import AudioSegment

from cursedboundapp.models import Background, Song, Encounter


@register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('display_name',)

    def view_on_site(self, obj):
        encounter = Encounter.objects.get(background=obj)
        return reverse('specific_encounter', kwargs={'id': encounter.pk})


@register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('display_name',)
    exclude = ('ogg_file',)

    def save_model(self, request, obj: Song, form, change) -> None:
        if 'mpeg_file' in form.changed_data:
            obj.save()
            seg = AudioSegment.from_mp3(obj.mpeg_file.open())
            name = obj.mpeg_file.name + '.ogg'
            f = io.BytesIO()
            seg.export(f, format='ogg')
            obj.ogg_file.save(name, f)

        super().save_model(request, obj, form, change)


@register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('display_name',)

    def display_name(self, obj: Encounter):
        return obj.background.display_name

    def view_on_site(self, obj):
        return reverse('specific_encounter', kwargs={'id': obj.pk})
