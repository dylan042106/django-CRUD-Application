from django.test import TestCase
from app import models


class TestSong(TestCase):
    def test_add_song(self):
        song_one = models.add_song(
            "All Time Low",
            "Jon Bellion",
            "The Human Condition",
            "Pop",
            True,
        )
        self.assertEqual(song_one.id, 1)
        self.assertEqual(song_one.name, "All Time Low")
        self.assertEqual(song_one.artist, "Jon Bellion")
        self.assertEqual(song_one.album, "The Human Condition")
        self.assertEqual(song_one.genre, "Pop")
        self.assertEqual(song_one.favorite, True)

    def test_find_song_by_name(self):
        song_data = [
            {
                "name": "Broadway Girls",
                "artist": "Lil Durk ft. Morgan Wallen",
                "album": "Broad",
                "genre": "Rap/Country",
                "favorite": False,
            },
            {
                "name": "Counting Stars",
                "artist": "OneRepublic",
                "album": "Native",
                "genre": "Pop",
                "favorite": True,
            },
            {
                "name": "Nervous",
                "artist": "John Legend",
                "album": "LEGEND",
                "genre": "Pop/Love",
                "favorite": True,
            },
            {
                "name": "How Do I Say Goodbye",
                "artist": "Dean Lewis",
                "album": "How Do I say Goodbye",
                "genre": "Sad/Heartbreak",
                "favorite": False,
            },
            {
                "name": "Not My Job Anymore",
                "artist": "Thomas Day",
                "album": "not my job anymore",
                "genre": "Heartbreak",
                "favorite": True,
            },
        ]

        for song_data in song_data:
            models.add_song(
                song_data["name"],
                song_data["artist"],
                song_data["album"],
                song_data["genre"],
                song_data["favorite"],
            )
        self.assertEquals(models.find_song_by_name("Goober"), "Song Does Not Exist!")
        song = models.find_song_by_name("Nervous")
        self.assertIsNotNone(song)
        self.assertEquals(song.artist, "John Legend")

    def test_favorite_songs(self):
        song_data = [
            {
                "name": "Broadway Girls",
                "artist": "Lil Durk ft. Morgan Wallen",
                "album": "Broad",
                "genre": "Rap/Country",
                "favorite": False,
            },
            {
                "name": "Counting Stars",
                "artist": "OneRepublic",
                "album": "Native",
                "genre": "Pop",
                "favorite": True,
            },
            {
                "name": "Nervous",
                "artist": "John Legend",
                "album": "LEGEND",
                "genre": "Pop/Love",
                "favorite": True,
            },
            {
                "name": "How Do I Say Goodbye",
                "artist": "Dean Lewis",
                "album": "How Do I say Goodbye",
                "genre": "Sad/Heartbreak",
                "favorite": False,
            },
            {
                "name": "Not My Job Anymore",
                "artist": "Thomas Day",
                "album": "not my job anymore",
                "genre": "Heartbreak",
                "favorite": True,
            },
        ]
        for song_data in song_data:
            models.add_song(
                song_data["name"],
                song_data["artist"],
                song_data["album"],
                song_data["genre"],
                song_data["favorite"],
            )

        self.assertEqual(len(models.favorite_songs()), 3)

    def test_delete_song(self):
        songs = [
            {
                "name": "Loves Lies",
                "artist": "Khalid ft Normani",
                "album": "Love Lies",
                "genre": "Pop/RnB",
                "favorite": False,
            },
            {
                "name": "Vette Motors",
                "artist": "NBA Youngboy",
                "album": "Top",
                "genre": "Rap/HipHop",
                "favorite": True,
            },
        ]
        for song_data in songs:
            models.add_song(
                song_data["name"],
                song_data["artist"],
                song_data["album"],
                song_data["genre"],
                song_data["favorite"],
            )
        models.delete_song("Vette Motors")

        self.assertEquals(len(models.all_songs()), 1)

    def test_update_artist(self):
        models.add_song("Without Me", "Halsey", "Manic", "Pop", True)
        models.update_artist("Without Me", "Halsey ft. Juice Wrld")

        self.assertEquals(
            models.find_song_by_name("Without Me").artist, "Halsey ft. Juice Wrld"
        )
