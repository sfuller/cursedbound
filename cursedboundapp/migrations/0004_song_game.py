# Generated by Django 2.1.7 on 2019-03-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursedboundapp', '0003_background_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='game',
            field=models.IntegerField(choices=[(0, 'Game.EARTHBOUND'), (1, 'Game.MOTHER'), (2, 'Game.MOTHER3')], default=0),
        ),
    ]