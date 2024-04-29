"""
This file contains the class for social interactions.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""
class SocialInteraction():
    """
    This class manages social interactions such as managing friends, following, and sharing songs with other users.
    """
    def __init__(self):
        pass
    
    def manage_friends(self, friend: User, action: str) -> None:
        """
        This method is used to manage a friend-related action such as adding or removing a friend.

        Args:
            friend (User): The user to add or remove as a friend.
            action (str): The action to perform, such as "add" or "remove".
        """
        pass

    def follow(self, entity: Union[User, Artist]) -> None:
        """
        This method is used to follow a user.

        Args:
            entity (Union[User, Artist]): The entity to follow.
        """    
        pass

    def share(self, song: Song, playlist: Playlist, to_user: User) -> None:
        """
        This method is used to share a song or playlist with another user.

        Args:
            song (Song): The song to share.
            playlist (Playlist): The playlist to share.
            to_user (User): The user with whom to share the song.
        """
        pass