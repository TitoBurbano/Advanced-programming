"""
This file contains the news class, which is responsible for notifications.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

class News:
    """This class is responsible for notifying users of new releases, or messages."""
    def __init__(self, message:str, sender: Optional[User] = None, recipient: Optional[User] = None):
        pass

    def send(self) -> None:
        """This method is used to send the notification."""
        pass

    def set_message(self, content: str) -> None:
        """
        This method is used to establish the content of the message that is to be sent.
        
        Args:
           content (str): The content of the message
        """
        pass

    def get_recipient(self) -> Optional[User]:
        """
        This method is used to obtain the information of the user who receipt the message.

        Returns:
              Optional [User]: User receiving the message, or a None.
        """
        pass

    def notify_release(self, song: Song, album: Album) -> None:
        """
        This method notifies about new releases.

        Args: 
           song (Song): The song that is launched.
           album (Album): The album that is launched.
        """
        pass

    def notify_shared(self, song: Song, playlist: Playlist, sender: User, recipient: User) -> None:
        """
        This method notifies about new shares.

        Args: 
           song (Song): The song that is shared.
           playlist (Playlist): The playlist that is shared.
           sender (User): The user who shares.
           recipient (User): The user who receives.
        """ 
        pass