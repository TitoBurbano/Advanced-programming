"""
This file contains the class that represents a user.

Author: Tito Burbano Plazas <titolaejandro3118@gmail.com>
"""

from typing import Union
from authentication import Authentication
from music_interaction import MusicInteraction
from profile import Profile
from social_interaction import SocialInteraction
from song import Song
from playlist import Playlist
from artist import Artist
from user import User as BaseUser  

class User:
    """
    This class represents a user with access to various features like authentication, 
    music interaction, profile customization, and social interaction.
    """

    def __init__(self, username: str, password: str, name: str, age: int, profile_pic: str):
      
        self.authentication = Authentication(username, password)
        self.music_interaction = MusicInteraction()
        self.profile = Profile(name, age, profile_pic)
        self.social_interaction = SocialInteraction()

    
    def sign_in(self) -> None:
        self.authentication.sign_in(self.authentication.username, self.authentication.password)

    def login(self) -> None:
        self.authentication.login(self.authentication.username, self.authentication.password)

    def customize_profile(self, new_name: str, new_age: int, new_profile_pic: str) -> None:
        self.profile.customize_profile(new_name, new_age, new_profile_pic)

    def search(self, keyword: str) -> list[Song]:
        return self.music_interaction.search(keyword)

    def create_playlist(self, playlist_name: str) -> Playlist:
        return self.music_interaction.create_playlist(playlist_name)

    def receive_suggestions(self) -> list[Song]:
        return self.music_interaction.receive_suggestions()

    def give_like(self, song: Song) -> None:
        self.music_interaction.give_like(song)

    def manage_friends(self, friend: BaseUser, action: str) -> None:
        self.social_interaction.manage_friends(friend, action)

    def follow(self, entity: Union[BaseUser, Artist]) -> None:
        self.social_interaction.follow(entity)

    def share(self, song: Song, to_user: BaseUser) -> None:
        self.social_interaction.share(song, to_user)

class Artist(User):
    """
    This class represents an artist.   
    """
    def __init__(self, username: str, password: str, name: str, age: int, profile_pic: str):
        super().__init__(username, password, name, age, profile_pic)

    def upload(self, song: Song, album: Album) -> None:
        """
        Uploads a new song or album for the artist.
        
        Args:
            song (Song): The song to be uploaded by the artist.
            album (Album): 
        """
        pass
