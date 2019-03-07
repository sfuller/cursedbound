# Generated by Django 2.1.7 on 2019-03-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursedboundapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='audio_file',
            new_name='mpeg_file',
        ),
        migrations.AddField(
            model_name='background',
            name='display_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='display_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='ogg_file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
