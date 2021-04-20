from user import User
import sqlite3 as sl

class UserData:
    def __init__(self, filepath):
        self.connection = sl.connect(filepath)

    def create(self, user):
        cursor = self.connection.cursor()

        cursor.execute("insert into user (username, password) values (?, ?)", (user.username, user.password))

        self.connection.commit()

        return user

    def findname(self, username):
        cursor = self.connection.cursor()

        cursor.execute("select * from user where username = ?", (username,))

        user = cursor.fetchone()

        return user

    def readall(self):
        cursor = self.connection.cursor()

        cursor.execute("select * from user")

        rows = cursor.fetchall()
        
        users = []

        for row in rows:
            users.append(User(row[0],row[1]))

        return users

    def deleteall(self):
        cursor = self.connection.cursor()

        cursor.execute("delete from user")

        self.connection.commit()

#user_data = UserData("src/data/data.db")