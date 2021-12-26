"""Handles the data storing
"""

import sqlite3 as sl
from entities.user import User

class UserRepository:
    """A class used to present user data storing into .db file.
    """

    def __init__(self, filepath):
        """Constructor of the class, creates connection to the database.

        Args:
            filepath:
                string: tells where the database is and it's name
            connection:
                Connection-object: creates the connection to the database.
        """

        self.connection = sl.connect(filepath)


    def create(self, user):
        """Creates a new user into the database

        Args:
            user: The user-object which is to be stored in the database.

        Returns:
            The stored user as user-object.
        """

        cursor = self.connection.cursor()

        cursor.execute("""insert into user
        (username, password, score) values (?, ?, 0)""", (user.username, user.password))

        self.connection.commit()

        return user

    def findname(self, username):
        """Returns user-object by its username.

        Args:
            username: Username of the user-object which is to be returned.

        Returns:
            Returns user-object if the username is in the database otherwise returns None.
        """

        cursor = self.connection.cursor()

        cursor.execute("select * from user where username = ?", (username,))

        user = cursor.fetchone()

        found_user = User(user[0], user[1]) if user else None

        return found_user

    def readall(self):
        """Returns all users from the database.

        Returns:
            Returns all users from the database as a list.
        """

        cursor = self.connection.cursor()

        cursor.execute("select * from user")

        rows = cursor.fetchall()

        users = []

        for row in rows:
            users.append((row[0],row[1], row[2]))

        return users

    def deleteall(self):
        """Removes all the users from the database
        """

        cursor = self.connection.cursor()

        cursor.execute("delete from user")

        self.connection.commit()

    def find_score_by_name(self, username):
        """Returns score from database by username.

        Args:
            username: Username of the user-object which is to be returned.

        Returns:
            Returns the hiscore of the user.
        """

        cursor = self.connection.cursor()

        cursor.execute("select score from user where username = ?", (username,))

        score = cursor.fetchone()

        found_score = score[0] if score else None

        return found_score

    def update_score(self, username, score):
        """Updates the hiscore of the user
        """

        cursor = self.connection.cursor()

        if self.find_score_by_name(username) < score:
            cursor.execute("UPDATE user SET score = ? WHERE username = ?", (score, username,))

        self.connection.commit()

    def read_all_top10_hiscore(self):
        """Returns 10 users from the database with the highest score.

        Returns:
            Returns 10 users from the database as a list.
        """

        cursor = self.connection.cursor()

        cursor.execute("select * from user ORDER BY score desc LIMIT 10")

        rows = cursor.fetchall()

        users = []

        for row in rows:
            users.append((row[0], row[2]))

        return users


# Location of the database file and the type of the file
user_repository = UserRepository("data.db")
