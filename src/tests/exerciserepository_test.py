import unittest
from repositories.exercise_repository import ExerciseRepository
from entities.exercise import Exercise

class TestUserData(unittest.TestCase):
    def setUp(self):
        self.exercise_data = ExerciseRepository("data/exercises.csv")
        self.exercise1 = Exercise("1+1","2", "Matti")
        self.exercise2 = Exercise("2+2", "4", "Keijo")
        
    def test_create(self):
        self.exercise_data.create(self.exercise1)
        data = self.exercise_data.readall()
        self.assertEqual(data[0][0], self.exercise1.question)
        
    def test_findname(self):
        self.exercise_data.create(self.exercise1)
        data = self.exercise_data.findname(self.exercise1.user)
        self.assertEqual(data[2], self.user1.username)

    def test_readall(self):
        self.exercise_data.create(self.exercise1)
        self.exercise_data.create(self.exercise2)
        data = self.exercise_data.readall()
        self.assertEqual(data[0][0],self.exercise1.question)
        self.assertEqual(data[1][0],self.exercise2.question)