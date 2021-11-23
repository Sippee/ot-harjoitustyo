from entities.user import User
import sqlite3 as sl


class UserRepository:

    """Luokka kuvaa käyttäjä tietojen tallennusta .db tiedostoon

    filepath: merkkijonoarvo, kertoo mihin ja millä nimellä tiedosto tallennetaan.
    """

    def __init__(self, filepath):
        self.connection = sl.connect(filepath)

    # Luodaan käyttäjä tietokantaan
    def create(self, user):
        cursor = self.connection.cursor()

        cursor.execute("insert into user (username, password) values (?, ?)", (user.username, user.password))

        self.connection.commit()

        return user

    # Etsitään tietokannasta nimellä palautetaan saadut arvot
    def findname(self, username):
        cursor = self.connection.cursor()

        cursor.execute("select * from user where username = ?", (username,))

        user = cursor.fetchone()

        return user

    # Luetaan koko tietokanta ja palautetaan listana koko tietokanta
    def readall(self):
        cursor = self.connection.cursor()

        cursor.execute("select * from user")

        rows = cursor.fetchall()
        
        users = []

        for row in rows:
            users.append(User(row[0],row[1]))

        return users

    # Tyhjennetään koko tietokanta
    def deleteall(self):
        cursor = self.connection.cursor()

        cursor.execute("delete from user")

        self.connection.commit()

# Tiedoston sijainti ja tyyppi
user_repository = UserRepository("data/data.db")