from typing import Union
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models import User as UserModel, Artist as ArtistModel, Song, Playlist
from ..news import News

class SocialInteraction:
    """
    This class manages social interactions such as managing friends, following, and sharing songs with other users.
    """

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.news = News()

    def manage_friends(self, user_id: int, friend_id: int, action: str) -> None:
        """
        This method is used to manage a friend-related action such as adding or removing a friend.

        Args:
            user_id (int): The ID of the user performing the action.
            friend_id (int): The ID of the friend to add or remove.
            action (str): The action to perform, such as "add" or "remove".
        """
        with self.Session() as session:
            user = session.query(UserModel).get(user_id)
            friend = session.query(UserModel).get(friend_id)
            if action.lower() == "add":
                if friend not in user.friends:
                    user.friends.append(friend)
                    session.commit()
                    print(f"{friend.name} has been added to your friends.")
                else:
                    print(f"{friend.name} is already your friend.")
            elif action.lower() == "remove":
                if friend in user.friends:
                    user.friends.remove(friend)
                    session.commit()
                    print(f"{friend.name} has been removed from your friends.")
                else:
                    print(f"{friend.name} is not in your friends.")

    def follow(self, user_id: int, entity_id: int, entity_type: str) -> None:
        """
        This method is used to follow a user or an artist.

        Args:
            user_id (int): The ID of the user following the entity.
            entity_id (int): The ID of the entity to follow.
            entity_type (str): The type of entity to follow, either "user" or "artist".
        """
        with self.Session() as session:
            user = session.query(UserModel).get(user_id)
            if entity_type == "user":
                entity = session.query(UserModel).get(entity_id)
            elif entity_type == "artist":
                entity = session.query(ArtistModel).get(entity_id)

            if entity not in user.following:
                user.following.append(entity)
                session.commit()
                print(f"Now following {entity.name}.")
            else:
                print(f"Already following {entity.name}.")

    def share(self, user_id: int, entity_id: int, entity_type: str, song_id: int = None, playlist_id: int = None) -> None:
        """
        This method is used to share a song or playlist with another user.

        Args:
            user_id (int): The ID of the user sharing the song or playlist.
            entity_id (int): The ID of the user with whom to share the song or playlist.
            entity_type (str): The type of entity to share with, either "user" or "artist".
            song_id (int): The ID of the song to share, if sharing a song. Defaults to None.
            playlist_id (int): The ID of the playlist to share, if sharing a playlist. Defaults to None.
        """
        with self.Session() as session:
            user = session.query(UserModel).get(user_id)
            if entity_type == "user":
                entity = session.query(UserModel).get(entity_id)
            elif entity_type == "artist":
                entity = session.query(ArtistModel).get(entity_id)

            if song_id:
                song = session.query(Song).get(song_id)
                notification = f"'{song.title}' has been shared with {entity.name}."
                self.news.add_notification(entity, notification)
                print(notification)
            elif playlist_id:
                playlist = session.query(Playlist).get(playlist_id)
                notification = f"Playlist '{playlist.name}' has been shared with {entity.name}."
                self.news.add_notification(entity, notification)
                print(notification)
