from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=20)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    favorite = models.BooleanField()


def add_song(name, artist, album, genre, favorite):
    new_song = Song(
        name=name, artist=artist, album=album, genre=genre, favorite=favorite
    )
    new_song.save()
    print(f"Successfully added { new_song.name } by { new_song.artist }")
    return new_song


def all_songs():
    return Song.objects.all()


def find_song_by_name(name):
    try:
        return Song.objects.get(name=name)
    except Song.DoesNotExist:
        return "Song Does Not Exist!"


def favorite_songs():
    return Song.objects.filter(favorite=True)


def update_artist(name, artist):
    selected_song = find_song_by_name(name)
    selected_song.artist = artist
    selected_song.save()


def delete_song(name):
    selected_song = find_song_by_name(name)
    selected_song.delete()
