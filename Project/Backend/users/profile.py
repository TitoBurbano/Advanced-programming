"""
This file contains the class representing a user profile.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models import User
from .authentication import Authentication

class Profile():
    """
    This class represents a user profile, which contains information such as name,
    age, and profile picture. It also provides functionality for customization.
    """
    def __init__(self, username: str, password: str, name: str, age: int, profile_pic: str):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.profile_pic = profile_pic

    @staticmethod
    def create_profile(username: str, password: str, name: str, age: Optional[int] = None, profile_pic: Optional[str] = None) -> 'Profile':
        """
        This method creates a new profile and saves user data to the database.

        Args:
            username (str): The username for the profile.
            password (str): The password for the profile.
            name (str): The name for the profile.
            age (Optional[int]): The age for the profile. Defaults to None.
            profile_pic (Optional[str]): The profile picture. Defaults to None.

        Returns:
            Profile: The newly created profile.
        """
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")

        if age is None:
            age = 0

        if profile_pic is None:
            profile_pic = "default.jpg"

        # Save user data to the database
        engine = create_engine("postgresql://usuario:contraseña@localhost/project_db")
        Session = sessionmaker(bind=engine)
        session = Session()
        user = User(username=username, password=password)
        session.add(user)
        session.commit()

        return Profile(username=username, password=password, name=name, age=age, profile_pic=profile_pic)

    def customize_profile(self, new_username: Optional[str] = None, new_password: Optional[str] = None, new_name: Optional[str] = None, new_age: Optional[int] = None, new_profile_pic: Optional[str] = None) -> None:
        """
        This method is used to customize the profile.

        Args:
            new_username (Optional[str]): The new username for the profile.
            new_password (Optional[str]): The new password for the profile.
            new_name (Optional[str]): The new name for the profile.
            new_age (Optional[int]): The new age for the profile.
            new_profile_pic (Optional[str]): A new profile picture.
        """
        if new_username is not None:
            if not new_username:
                raise ValueError("Username cannot be empty.")
            self.username = new_username

        if new_password is not None:
            if not new_password:
                raise ValueError("Password cannot be empty.")
            self.password = new_password

        if new_name is not None:
            self.name = new_name

        if new_age is not None:
            if new_age < 0:
                raise ValueError("Age must be a positive number.")
            self.age = new_age

        if new_profile_pic is not None:
            self.profile_pic = new_profile_pic

        print("Profile has been customized.")
