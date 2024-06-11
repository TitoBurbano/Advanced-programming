"""
This file contains the information of the authentication class.
"""

import hashlib
import psycopg2

class Authentication:
    """
    The authentication class checks the login and registration of users to Musicat.
    """
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def register(self, username, password):
        """
        This method creates a new user.

        Args:
        username (str): Username.
        password (str): Password.

        Returns:
        str: Success or error message.
        """
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_password)
            )
            self.connection.commit()
            return "User registered successfully"
        except psycopg2.IntegrityError:
            self.connection.rollback()
            return "Username already exists"

    def login(self, username, password):
        """
        This method verifies that the data is correct and allows the user to enter.

        Args:
        username (str): Username.
        password (str): Password.

        Returns:
        str: Success or error message.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, hashed_password)
        )
        user = self.cursor.fetchone()
        if user:
            return "Login successful"
        else:
            return "Invalid username or password"

    def __del__(self):
        self.cursor.close()
        self.connection.close()


auth = Authentication(dbname="project_db", user="postgres", password="postgres")
