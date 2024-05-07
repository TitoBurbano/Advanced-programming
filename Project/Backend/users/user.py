"""
This file contains the class that represents a user.

Author: Tito Burbano Plazas <titolaejandro3118@gmail.com>
"""

from typing import Union, List
from ..music import Song, Playlist, Album  
from ..users import Authentication, MusicInteraction, Profile, SocialInteraction
from news import News

class User:
    """
    This class represents a user with access to various features like authentication,
    music interaction, profile customization, and social interaction.
    """

    def __init__(self, username: str, password: str, name: str, age: int, profile_pic: str):
        self.username = username  
        self.password = password  
        self.authentication = Authentication()  
        self.music_interaction = MusicInteraction()
        self.profile = Profile.create_profile(name, age, profile_pic) 
        self.social_interaction = SocialInteraction() 

    def sign_in(self) -> Profile:
        """Signs in a new user and creates a profile."""
        return self.authentication.sign_in(self.username, self.password)

    def login(self) -> None:
        """Logs in an existing user."""
        self.authentication.login(self.username, self.password)

    def customize_profile(self, new_name: str, new_age: int, new_profile_pic: str) -> None:
        """Customizes the user's profile."""
        self.profile.customize_profile(new_name, new_age, new_profile_pic)

    def search(self, keyword: str) -> List[Song]:
        """Searches for songs based on a keyword."""
        return self.music_interaction.search(keyword)

    def create_playlist(self, playlist_name: str) -> Playlist:
        """Creates a new playlist."""
        return self.music_interaction.create_playlist(playlist_name)

    def receive_suggestions(self) -> List[Song]:
        """Receives song suggestions based on user preferences or history."""
        return self.music_interaction.receive_suggestions()

    def give_like(self, song: Song) -> None:
        """Gives a like to a song, indicating user preference."""
        self.music_interaction.give_like(song)

    def manage_friends(self, friend: User, action: str) -> None:
        """Adds or removes a friend based on the specified action."""
        self.social_interaction.manage_friends(friend, action)

    def follow(self, entity: Union[User, Artist]) -> None:
        """Follows another user or artist."""
        self.social_interaction.follow(entity)

    def share(self, song: Song, to_user: User) -> None:
        """Shares a song with another user."""
        self.social_interaction.share(song, to_user)

class Artist(User):
    """
    This class represents an artist, inheriting from User, with additional functionality to upload songs and albums.
    """

    def __init__(self, username: str, password: str, name: str, age: int, profile_pic: str):
        super().__init__(username, password, name, age, profile_pic)

    def upload_song(self, song: Song) -> None:
        """
        Allows the artist to upload a new song.

        Args:
            song (Song): The song to be uploaded by the artist.
        """
        print(f"Song '{song.title}' uploaded by artist '{self.profile.name}'.")
        self.news.send(
            message=f"New song '{song.title}' uploaded by {self.profile.name}.",
            sender=self,
            recipient=None  
        )

    def upload_album(self, album: Album) -> None:
        """
        Allows the artist to upload a new album.

        Args:
            album (Album): The album to be uploaded by the artist.
        """
        print(f"Album '{album.title}' uploaded by artist '{self.profile.name}'.")
        self.news.send(
            message=f"New album '{album.title}' uploaded by {self.profile.name}.",
            sender=self,
            recipient=None  
        )

