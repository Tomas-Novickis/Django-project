# Generated by Django 4.2 on 2023-04-25 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_rename_genre_game_genres_remove_game_user_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='users',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
