from entities.user import User
from repositories.user_repository import user_repository as default_user_repository

class UserError(Exception):

    """Luokka on poikkeus
    Käytämme poikkeusta virheilmoituksena
    """

    pass

class Service:

    """Luokka kuvaa sovelluksenlogiikan"""

    def __init__(self, user_repository = default_user_repository):

        """Sovelluslogiikasta vastaavan luokan konstruktori.
        Args:
            user_repository:
                Vapaehtoinen
                UserRepository-olio, joka omaa UserRepository luokan metodit
        """

        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login = True):

        """Luodaan uusi käyttäjä
        Args:
            username: Merkkijonoarvo, kuvaa käyttäjän käyttäjätunnusta
            password: Merkkijonoarvo, kuvaa käyttäjän salasanaa
        Returns:
            Kyseisen käyttäjän User-oliona
        Raises:
            UserError:
                Virhe uuden käyttäjän rekisteröinnissä
        """

        username_available = self._user_repository.findname(username)
        if username_available is not None and username_available[0] == username:
            raise UserError("This username is already used")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):

        """Kirjaudutaan käyttäjä sovelluksen sisälle
        Args:
            username: Merkkijonoarvo, kuvaa käyttäjän käyttäjätunnusta
            password: Merkkijonoarvo, kuvaa käyttäjän salasanaa
        Returns:
            Kirjautuvan käyttäjän User-oliona
        Raises:
            UserError:
                Virhe kirjautuessa
        """

        user = self._user_repository.findname(username)

        if not user or user[1] != password:
            raise UserError("Either Username or Password is invalid")

        self._user = user
        
        return user

    def get_user(self):

        """
        Returns:
            Kirjautuneen käyttäjän User oliona
        """

        return self._user

    def get_users(self):

        """
        Returns:
            Kaikki User oliot listana.
        """

        return self._user_repository.readall()

    def logout(self):

        """Kirjaa kirjautuneen käyttäjän ulos sovelluksesta"""

        self._user = None

service = Service()