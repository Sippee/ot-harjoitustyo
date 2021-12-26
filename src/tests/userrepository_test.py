import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserData(unittest.TestCase):
    def setUp(self):
        user_repository.deleteall()
        self.user1 = User("Matti","keijotin")
        self.user2 = User("Keijo", "kaspertin")
        
    def test_create(self):
        user_repository.create(self.user1)
        data = user_repository.readall()
        self.assertEqual(data[0][0], self.user1.username)
        
    def test_findname(self):
        user_repository.create(self.user1)
        data = user_repository.findname(self.user1.username)
        self.assertEqual(data.username, self.user1.username)

    def test_readall(self):
        user_repository.create(self.user1)
        user_repository.create(self.user2)
        data = user_repository.readall()
        self.assertEqual(data[0][0],self.user1.username)
        self.assertEqual(data[1][0],self.user2.username)

    def test_find_score_by_name(self):
        user_repository.create(self.user1)
        data = user_repository.find_score_by_name(self.user1.username)
        self.assertEqual(data, 0)

    def test_update_score_over_0(self):
        user_repository.create(self.user1)
        user_repository.update_score(self.user1.username, 1)
        data = user_repository.find_score_by_name(self.user1.username)
        self.assertEqual(data,1)

    def test_update_score_exactly_0(self):
        user_repository.create(self.user1)
        user_repository.update_score(self.user1.username, 0)
        data = user_repository.find_score_by_name(self.user1.username)
        self.assertEqual(data,0)

    def test_read_top10(self):
        user_repository.create(self.user1)
        user_repository.update_score(self.user1.username, 1)
        data = user_repository.read_all_top10_hiscore()
        self.assertEqual(data[0][1],1)
