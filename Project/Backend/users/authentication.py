import hashlib
import psycopg2
from psycopg2 import sql
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
        self.conn = psycopg2.connect(db_url)
        self.cursor = self.conn.cursor()

   def sign_in(self, username: str, password: str):
        """
        Registers a new user in the system with a specified username and password.

        Args:
           username (str): The desired username for the new user.
           password (str): The password for the new user.
        """
        Profile.create_profile(username)

        return {"username": username, "profile_pic": None}

    def login(self, username: str, password: str) -> dict:
        """
        Authenticates a user to log into the system with their account credentials.

        Args:
            username (str): The username for login.
            password (str): The password for login.

        Returns:
            dict: The response containing user data.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = sql.SQL("SELECT username FROM users WHERE username = %s AND password = %s;")
        self.cursor.execute(query, (username, hashed_password))
        result = self.cursor.fetchone()
        if result:
            return {"username": result[0], "profile_pic": None}
        else:
            raise ValueError("Invalid username or password.")

    def close(self):
        """
        Closes the database connection.
        """
        self.cursor.close()
        self.conn.close()


        