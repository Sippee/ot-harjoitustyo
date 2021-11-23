class User:

    """Luokka kuvaa yhtä käyttäjää

    username: Merkkijonoarvo, käyttäjän käyttäjätunnus
    password: Merkkijonoarvo, käyttäjän salasana
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password