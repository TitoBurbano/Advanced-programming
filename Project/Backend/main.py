"""
Main file where web services are located.

Author: Tito Alejandro Burbano Plazas <titoalejandro3118@gmail.com>
"""
from fastapi import FastAPI
from music import Genre, Playlist
from users import User, Authentication

app = FastAPI()

genre_instance = Genre(name="default")
playlist = Playlist(name="default")
authentication = Authentication(
    dbname="project_db",
    user="postgres",
    password="postgres"
)

user = User(username="default")

@app.get("/genre/{genre_name}/songs")
def get_genre_songs(genre_name: str):
    """
    Gets all songs of a specific genre.
    Call method get_genre_songs in Genre class.
    """
    genre_instance.name = genre_name
    return genre_instance.get_genre_songs()

@app.post("/playlist/{playlist_name}/add-song")
def add_song_to_playlist(playlist_name: str, song_title: str):
    """
    Add a song to a specific playlist.
    Call the method add_song in the Playlist class.
    """
    playlist.name = playlist_name
    return playlist.add_song(song_title)

@app.delete("/playlist/{playlist_name}/remove-song")
def remove_song_from_playlist(playlist_name: str, song_title: str):
    """
    Remove a song from a specific playlist.
    Call the method remove song in the Playlist class.
    """
    playlist.name = playlist_name
    return playlist.remove_song(song_title)

@app.get("/playlist/{playlist_name}/songs")
def get_playlist_songs(playlist_name: str):
    """
    Gets all the songs in a specific playlist.
    Call the method get_playlist_songs in the Playlist class
    """
    playlist.name = playlist_name
    return playlist.get_playlist_songs()

@app.post("/register")
def register(username: str, password: str):
    """
    Register a new user.
    Call the method register in the Authentication class
    """
    return authentication.register(username, password)

@app.post("/login")
def login(username: str, password: str):
    """
    Log in with a registered user.
    Call the method login in the Authentication class
    """
    return authentication.login(username, password)

@app.get("/search")
def search(keyword: str):
    """
    Search songs by keyword.
    Call the method search in the User class.
    """
    return user.search(keyword)

@app.post("/create-playlist")
def create_playlist(playlist_name: str):
    """
    Create a new playlist.
    Call the method create_playlist in the User class.
    """
    user.username = " "  
    return user.create_playlist(playlist_name)

@app.post("/add-song-to-playlist")
def add_song_to_a_playlist(playlist_name: str, song_title: str):
    """
    Add a song to a specific playlist.
    Call the method add_song_to_playlist in the User class.
    """
    user.username = "default"  
    return user.add_song_to_playlist(playlist_name, song_title)

@app.post("/upload-song")
def upload_song(title: str, artist: str, genre: str, duration: str, album: str, url: str):
    """
    Upload a new song.
    Call the method upload_song in the User class.
    """
    return user.upload_song(title, artist, genre, duration, album, url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)