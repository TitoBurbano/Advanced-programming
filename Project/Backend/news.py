"""
This file contains the news class, which is responsible for notifications.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import Optional, List
from .users import User
from .music import Song, Album, Playlist  
#from database import Database  
import datetime  

class News:
    """
    This class is responsible for notifying users of new releases or messages.
    """

    def __init__(self):
        self.notifications = []  
        #self.database = Database()  

    def send(self, message: str, sender: Optional[User] = None, recipient: Optional[User] = None) -> None:
        """This method sends the notification"""
        
        notification = {
            "message": message,
            "sender": sender.username if sender else None,
            "recipient": recipient.username if recipient else None,
            "timestamp": datetime.datetime.now()  # Fecha y hora de la notificación
        }

        #self.notifications.append(notification)

        #self.database.store_notification(notification)

    def get_notifications(self) -> List[dict]:
        """
        This method returns all stored notifications.

        Returns:
            List[dict]: List of all stored notifications.
        """
        return self.notifications  