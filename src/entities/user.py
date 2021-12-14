class User:
    """A class used to present one user
    """

    def __init__(self, username, password):
        """Constructor of the class, creates new user.

        Args:
            username: String, the username of the user
            password: String, the password of the user
        """

        self.username = username
        self.password = password