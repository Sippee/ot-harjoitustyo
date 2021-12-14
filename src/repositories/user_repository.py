from entities.user import User
import sqlite3 as sl


class UserRepository:
    """A class used to present user data storing into .db file.
    """

    def __init__(self, filepath):
        """Constructor of the class, creates connection to the database.

        Args:
            filepath: 
                string, tells where the database is and it's name
            connection:
                Connection-object, which creates the connection to the database.
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

        cursor.execute("insert into user (username, password) values (?, ?)", (user.username, user.password))

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
            Returns all users from the databased as a list.
        """

        cursor = self.connection.cursor()

        cursor.execute("select * from user")

        rows = cursor.fetchall()
        
        users = []

        for row in rows:
            users.append(User(row[0],row[1]))

        return users

    def deleteall(self):
        """Removes all the users from the database
        """

        cursor = self.connection.cursor()

        cursor.execute("delete from user")

        self.connection.commit()

# Tiedoston sijainti ja tyyppi
user_repository = UserRepository("data.db")
