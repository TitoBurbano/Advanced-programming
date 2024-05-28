"""
This file contains the class for user authentication operations.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .schemes import UserResponse
from ..models import User
from .profile import Profile
class Authentication:
    """
    This class manages user authentication operations, including registration 
    and login.
    """

    def __init__(self, db_url: str):
        """
        Initializes the Authentication class with the database URL and name.

        Args:
            db_url (str): The URL for connecting to the PostgreSQL database.
        """
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def sign_in(self, username: str, password: str) -> UserResponse:
        """
        Registers a new user in the system with a specified username and password.

        Args:
           username (str): The desired username for the new user.
           password (str): The password for the new user.

        Returns:
            UserResponse: The response containing user data.
        """
        user = User(username=username, password=password)
        self.session.add(user)
        self.session.commit()
        
        Profile.create_profile(username)
        
        return UserResponse(username=username, profile_pic=None)

    def login(self, username: str, password: str) -> UserResponse:
        """
        Authenticates a user to log into the system with their account credentials.

        Args:
           username (str): The username for login.
           password (str): The password for login.

        Returns:
            UserResponse: The response containing user data.
        """
        user = self.session.query(User).filter_by(username=username, password=password).first()
        if user:
            return UserResponse(username=user.username, profile_pic=None)
        else:
            raise ValueError("Invalid username or password.")




        