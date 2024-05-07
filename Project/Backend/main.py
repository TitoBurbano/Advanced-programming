from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .users import User, Artist, Profile, Authentication, SocialInteraction
from .music import Song, Playlist, Album
from news import News

app = FastAPI()

class UserCredentials(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(credentials: UserCredentials):
    """
    This endpoint validates if a user is valid or not.

    Args:
        credentials (UserCredentials): Username and password of the user.
    """
    try:
        user = User.login(credentials.username, credentials.password)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/create_artist")
def create_artist(artist: Artist) -> bool:
    """
    This endpoint lets create a new artist.

    Args:
        artist (Artist): Artist to be added.
    """
    print(f"Artist '{artist.profile.name}' has been created.")
    return True

@app.post("/share_song")
def share_song(data: dict):
    """
    This endpoint allows sharing a song with another user.

    Args:
        data (dict): Contains 'song' and 'recipient'.
    """
    song = Song(data["song_code"], data["title"], data["author"], data["genre"], data["length"], data["album"], data["release_date"], data["audio_url"])
    recipient = User(data["recipient_username"], data["recipient_password"], data["recipient_name"], data["recipient_age"], data["recipient_profile_pic"])

    social = SocialInteraction()
    social.share(song=song, sender=Artist("john_doe", "password", "John Doe", 30, "profile.jpg"), recipient=recipient)

    return {"status": "Song shared"}

@app.post("/artist/upload_song")
def upload_song(artist_data: dict, song_data: dict):
    """
    This endpoint allows an artist to upload a song.

    Args:
        artist_data (dict): Contains artist details.
        song_data (dict): Contains song details.
    """
    artist = Artist(artist_data["username"], artist_data["password"], artist_data["name"], artist_data["age"], artist_data["profile_pic"])
    song = Song(song_data["song_code"], song_data["title"], song_data["author"], song_data["genre"], song_data["length"], song_data["album"], song_data["release_date"], song_data["audio_url"])

    artist.upload_song(song)

    return {"status": f"Song '{song.title}' uploaded by {artist.profile.name}"}

@app.post("/user/create_playlist")
def create_playlist(playlist_name: str, user_data: dict):
    """
    This endpoint allows a user to create a playlist.

    Args:
        playlist_name (str): Name of the new playlist.
        user_data (dict): User information to identify the creator.
    """
    user = User(user_data["username"], user_data["password"], user_data["name"], user_data["age"], user_data["profile_pic"])
    playlist = user.music_interaction.create_playlist(playlist_name)

    return {"status": "Playlist created", "playlist": playlist.name}

@app.get("/user/search_songs")
def search_songs(keyword: str):
    """
    This endpoint allows a user to search for songs based on a keyword.

    Args:
        keyword (str): The keyword used for the search.
    """
    user = User("john_doe", "password", "John Doe", 25, "profile.jpg")  
    results = user.search(keyword)

    return {"status": "Search results", "songs": [song.title for song in results]}

@app.post("/user/give_like")
def give_like(song_code: int):
    """
    This endpoint allows a user to give a like to a song.

    Args:
        song_code (int): The code of the song to be liked.
    """
    user = User("john_doe", "password", "John Doe", 25, "profile.jpg")
    user.give_like(Song(song_code, "Song Title", "Author", "Genre", 200, "Album", False, "http://example.com/song.mp3"))

    return {"status": "Song liked"}

@app.post("/user/share_song")
def share_song(song_code: int, recipient_data: dict):
    """
    This endpoint allows a user to share a song with another user.

    Args:
        song_code (int): The code of the song to be shared.
        recipient_data (dict): Information about the recipient user.
    """
    song = Song(song_code, "Song Title", "Author", "Genre", 200, "Album", False, "http://example.com/song.mp3")
    recipient = User(recipient_data["username"], recipient_data["password"], recipient_data["name"], recipient_data["age"], recipient_data["profile_pic"])

    social = SocialInteraction()
    social.share(song=song, sender=None, recipient=recipient)

    return {"status": "Song shared with " + recipient.profile.name}
