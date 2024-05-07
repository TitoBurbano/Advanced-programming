"""
This file contains the class for social interactions.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import Union, List
from .user import User, Artist  
from ..music import Song, Playlist
from ..news import News

class SocialInteraction:
    """
    This class manages social interactions such as managing friends, following, and sharing songs with other users.
    """

    def __init__(self):
        self.friends = []  
        self.following = []
        self.news = News()  

    def manage_friends(self, friend: User, action: str) -> None:
        """
        This method is used to manage a friend-related action such as adding or removing a friend.

        Args:
            friend (User): The user to add or remove as a friend.
            action (str): The action to perform, such as "add" or "remove".
        """
        if action.lower() == "add":
            if friend not in self.friends:
                self.friends.append(friend)
                print(f"{friend.name} has been added to your friends.")
            else:
                print(f"{friend.name} is already your friend.")
        elif action.lower() == "remove":
            if friend in self.friends:
                self.friends.remove(friend)
                print(f"{friend.name} has been removed from your friends.")
            else:
                print(f"{friend.name} is not in your friends.")

    def follow(self, entity: Union[User, Artist]) -> None:
        """
        This method is used to follow a user or an artist.

        Args:
            entity (Union[User, Artist]): The entity to follow.
        """    
        if entity not in self.following:
            self.following.append(entity)
            print(f"Now following {entity.name}.")
        else:
            print(f"Already following {entity.name}.")

    def share(self, song: Song = None, playlist: Playlist = None, to_user: User) -> None:
        """
        This method is used to share a song or playlist with another user.

        Args:
            song (Song): The song to share.
            playlist (Playlist): The playlist to share.
            to_user (User): The user with whom to share the song or playlist.
        """
        if song:
            notification = f"'{song.title}' has been shared with {to_user.name}."
            self.news.add_notification(to_user, notification)  
            print(notification)
        
        if playlist:
            notification = f"Playlist '{playlist.name}' has been shared with {to_user.name}."
            self.news.add_notification(to_user, notification)  
            print(notification)
