import unittest
from entities.user import User
from services import service
from services.service import Service, UserError

class FakeUserRepository:
    def __init__(self, users=None, scores=None):
        self.users = users or []
        self.scores = scores or []

    def readall(self):
        return self.users

    def findname(self, username):
        matches = filter(
            lambda user: user.username == username, self.users)

        list_of_matches = list(matches)

        return list_of_matches[0] if len(list_of_matches) > 0 else None

    def create(self, user):
        self.users.append(user)
        self.scores.append((user.username, 0))

        return user

    def deleteall(self):
        self.users = []

    def read_all_top10_hiscore(self):
        users = []

        for row in self.scores:
            if row[1] > 0:
                users.append((row[0], row[1]))

        return users

    def update_score(self, username, score):
        new_scores = []
        for row in self.scores:
            if row[0] == username:
                row = (username, score)
                new_scores.append(row)
            else:
                new_scores.append(row)
        self.scores = new_scores

class TestService(unittest.TestCase):
    def setUp(self):
        self.repository = FakeUserRepository()
        self.service = Service(self.repository)
        self.user1 = User("Matti","keijotin")
        self.user2 = User("Keijo","Mattin")
        
    def test_create_user(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password, 0)

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

    def test_top10_hiscore_empty(self):
        username = self.user1.username
        password = self.user1.password
        username2 = self.user2.username
        password2 = self.user2.password

        self.repository.create(User(username,password))
        self.repository.create(User(username2,password2))
        self.assertEqual(len(self.service.top10_hiscore()), 0)

    def test_maingame(self):
        username = self.user1.username
        password = self.user1.password

        self.service.create_user(username, password)
        self.service.login(username, password)

        data = self.service.game(1)

        self.assertEqual(data, 0)

    def test_top10_hiscore_not_empty(self):
        username = self.user1.username
        password = self.user1.password

        self.repository.create(User(username,password))
        self.repository.update_score(username, 1)

        self.assertEqual(len(self.service.top10_hiscore()), len(self.repository.scores))
