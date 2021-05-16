from entities.exercise import Exercise
from entities.user import User
from repositories.exercise_repository import exercise_repository as default_exercise_repository
from repositories.user_repository import user_repository as default_user_repository

class UserError(Exception):

    """Luokka on poikkeus
    Käytämme poikkeusta virheilmoituksena
    """

    pass

class Service:

    """Luokka kuvaa sovelluksenlogiikan"""

    def __init__(self, exercise_repository = default_exercise_repository, user_repository = default_user_repository):

        """Sovelluslogiikasta vastaavan luokan konstruktori.
        Args:
            exercise_repository:
                Vapaaehtoinen
                ExerciseRepository-olio, joka omaa ExerciseRepository luokan metodit
            user_repository:
                Vapaehtoinen
                UserRepository-olio, joka omaa UserRepository luokan metodit
        """

        self._user = None
        self._exercise_repository = exercise_repository
        self._user_repository = user_repository

    def create_exercise(self, question, answer):

        """Luodaan uusi tehtävä
        Args:
            question: Merkkijonoarvo, kuvaa tehtävän kysymyksen
            answer: Merkkijonoarvo, kuvaa tehtävän vastauksen
        Returns:
            Kyseisen tehtävän Exercise-oliona
        """

        exercise = Exercise(question, answer, user=self._user)
        
        return self._exercise_repository.create(exercise)

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

    def get_exercises(self):

        """Palauttaa käyttäjän lisäämät tehtävät
        Returns:
            Käyttäjän lisäämät tehtävät Exercise-olioden listana
            tai se palauttaa tyhjän listan, jos käyttäjää ei ole

        """

        if not self._user:
            return []

        try:
            exercises = self._exercise_repository.findname(self._user.username)
        except:
            exercises = self._exercise_repository.findname(self._user[0])

        return list(exercises)

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