"""
This file contains the class representing a user profile.

Author: Tito Burbano Plazas <titoalejandro3118@gmail.com>
"""

from typing import Optional

class Profile():
    """
    This class represents a user profile, which contains information such as name,
    age, and profile picture. It also provides functionality for customization.
    """
    def __init__(self, name: str, age: int, profile_pic: str):
        self.name = name
        self.age = age
        self.profile_pic = profile_pic

    @staticmethod
    def create_profile(name: str, age: Optional[int] = None, profile_pic: Optional[str] = None) -> 'Profile':
        """
        This method creates a new profile, allowing customization.

        Args:
            name (str): The name for the profile.
            age (Optional[int]): The age for the profile. Defaults to 18.
            profile_pic (Optional[str]): The profile picture. Defaults to "default.jpg".

        Returns:
            Profile: The newly created profile.
        """
        if not name:
            raise ValueError("Name cannot be empty.")

        if age is None:
            age = 0

        if profile_pic is None:
            profile_pic = "default.jpg"

        return Profile(name=name, age=age, profile_pic=profile_pic)
    
    def customize_profile(self, new_name: Optional[str] = None, new_age: Optional[int] = None, new_profile_pic: Optional[str] = None) -> None:
        """
        This method is used to customize the profile.

        Args:
            new_name (Optional[str]): The new name for the profile.
            new_age (Optional[int]): The new age for the profile.
            new_profile_pic (Optional[str]): A new profile picture.
        """
        if new_name is not None:
            if not new_name:
                raise ValueError("Name cannot be empty.")
            self.name = new_name

        if new_age is not None:
            if new_age < 0:
                raise ValueError("Age must be a positive number.")
            self.age = new_age

        if new_profile_pic is not None:
            self.profile_pic = new_profile_pic

        print("Profile has been customized.")
