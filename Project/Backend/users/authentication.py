"""
This file contains the class for user authentication operations.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""
from pydantic import BaseModel
from .profile import Profile
class Authentication(BaseModel):
    """
    This class manages user authentication operations, including registration 
    and login.
    """
    username: str
    password: str
    
    def sign_in(self, username: str, password: str) -> None:
        """
        Registers a new user in the system with a specified username and password.

        Args:
           username (str): The desired username for the new user.
           password (str): The password for the new user.
        """
        if any(user['username'] == username for user in self.users):
            raise ValueError("Username already exists.")

        new_user = {"username": username, "password": password}
        self.users.append(new_user)

        return Profile.create_profile(username)

    
    def login(self, username: str, password: str) -> None:
        """
        Authenticates a user to log into the system with their account credentials.

        Args:
           username (str): The username for login.
           password (str): The password for login.
        """
        print('...')
        