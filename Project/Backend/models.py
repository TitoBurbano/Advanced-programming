from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    profile_pic = Column(String, nullable=True)
    
    playlists = relationship("Playlist", back_populates="owner")
    liked_songs = relationship("Song", secondary="user_like_song")
    
    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    genre = Column(String, index=True)
    length = Column(Integer)
    audio_url = Column(String)

    albums = relationship("Album", back_populates="songs")
    liked_by_users = relationship("User", secondary="user_like_song")

    def __repr__(self):
        return f"<Song(title='{self.title}', artist='{self.artist}')>"
    

class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    release_date = Column(String)

    songs = relationship("Song", back_populates="albums")

    def __repr__(self):
        return f"<Album(title='{self.title}', artist='{self.artist}')>"

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    songs = relationship("Song", back_populates="genre")

    def __repr__(self):
        return f"<Genre(name='{self.name}')>"

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="playlists")
    songs = relationship("Song", secondary="playlist_song")

    def __repr__(self):
        return f"<Playlist(name='{self.name}', owner='{self.owner.username}')>"

class UserLikeSong(Base):
    __tablename__ = 'user_like_song'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)

class PlaylistSong(Base):
    __tablename__ = 'playlist_song'

    playlist_id = Column(Integer, ForeignKey('playlists.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)

