import unittest
from entities.user import User
from services.service import Service, UserError

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def readall(self):
        return self.users

    def findname(self, username):
        matches = filter(
            lambda user: user.username == username, self.users)

        list_of_matches = list(matches)

        return list_of_matches[0] if len(list_of_matches) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def deleteall(self):
        self.users = []

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(FakeUserRepository())
        self.user1 = User("Matti","keijotin")
        
    def test_create_user(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password)

        users = self.service.get_users()

        self.assertEqual(users[0].username, username)

    def test_create_user_that_exists(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password)

        self.assertRaises(UserError, lambda: self.service.create_user(username, "abc"))

    def test_login(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password)

        logged_in_user = self.service.login(username, password)

        self.assertEqual(logged_in_user.username, username)

    def test_invalid_login(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password)

        self.assertRaises(UserError, lambda: self.service.login("abc123", "abc123"))

    def test_get_user(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password)

        self.service.login(username, password)

        user = self.service.get_user()

        self.assertEqual(user.username, username)

    def test_logout(self):
        self.service.logout()
        self.assertEqual(self.service.get_user(), None)