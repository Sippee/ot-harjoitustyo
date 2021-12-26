from entities.user import User
from repositories.user_repository import user_repository as default_user_repository
from collectinggame.coincollector import main_game

class UserError(Exception):
    """A exception class that we can use as a error message
    """

    pass

class Service:
    """A class used to present the application logic.
    """

    def __init__(self, user_repository = default_user_repository):
        """Constructor of the class, which handles the application logic.

        Args:
            user_repository:
                Optional
                UserRepository-object, which handles reading and writing to the database
        """

        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login = True):
        """Creates a new user

        Args:
            username: String, presents the username of the user
            password: String, presents the password of the user

        Returns:
            The created user

        Raises:
            UserError:
                Error while creating new user
        """

        username_available = self._user_repository.findname(username)
        if username_available is not None and username_available.username == username:
            raise UserError("This username is already used")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def login(self, username, password):
        """The user logging in the application

        Args:
            username: String, presents the username of the user
            password: String, presents the password of the user

        Returns:
            The user that logged in

        Raises:
            UserError:
                Error while logging in
        """

        user = self._user_repository.findname(username)

        if not user or user.password != password:
            raise UserError("Either Username or Password is invalid")

        self._user = user
        
        return user

    def get_user(self):
        """
        Returns:
            The user that is logged in
        """

        return self._user

    def get_users(self):
        """
        Returns:
            All user-objects as a list.
        """

        return self._user_repository.readall()

    def logout(self):
        """Logs the user, that is logged in, out from the application
        """

        self._user = None

    def game(self):
        """Runs the main game, tries update the score on the database

        Returns:
            collected_points: How many points the player collected during the game
        """
        collected_points = main_game()
        
        self._user_repository.update_score(self._user.username, collected_points)
        
        return collected_points

    
    def top10_hiscore(self):
        """
        Returns:
            10 user-objects as a list which have the highest score.
        """

        top10 = []
        for user in self._user_repository.read_all_top10_hiscore():
            score = user[1]
            name = user[0]
            if int(score) > 0:
                top10.append(f"{name:<30} {score:3d}")

        return top10
    

service = Service()
