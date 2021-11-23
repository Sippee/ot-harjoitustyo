import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserData(unittest.TestCase):
    def setUp(self):
        self.user_data = UserRepository("data/data.db")
        self.user_data.deleteall()
        self.user1 = User("Matti","keijotin")
        self.user2 = User("Keijo", "kaspertin")
        
    def test_create(self):
        self.user_data.create(self.user1)
        data = self.user_data.readall()
        self.assertEqual(data[0].username, self.user1.username)
        
    def test_findname(self):
        self.user_data.create(self.user1)
        data = self.user_data.findname(self.user1.username)
        self.assertEqual(data[0], self.user1.username)

    def test_readall(self):
        self.user_data.create(self.user1)
        self.user_data.create(self.user2)
        data = self.user_data.readall()
        self.assertEqual(data[0].username,self.user1.username)
        self.assertEqual(data[1].username,self.user2.username)