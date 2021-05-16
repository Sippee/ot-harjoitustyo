import unittest
from repositories.exercise_repository import ExerciseRepository
from entities.exercise import Exercise

class TestExerciseData(unittest.TestCase):
    def setUp(self):
        self.exercise_data = ExerciseRepository("data/testexercises.csv")
        self.exercise1 = Exercise("1+1","2","Matti")
        self.exercise2 = Exercise("2+2", "4","Keijo")
        
    def test_create(self):
        self.exercise_data.create(self.exercise1)
        data = self.exercise_data.readall()
        self.assertEqual(data[0].question, self.exercise1.question)
        
    def test_findname(self):
        self.exercise_data.create(self.exercise1)
        data = self.exercise_data.findname(self.exercise1.user)
        self.assertEqual(data[2], self.exercise1.user)

    def test_readall(self):
        self.exercise_data.create(self.exercise1)
        self.exercise_data.create(self.exercise2)
        data = self.exercise_data.readall()
        self.assertEqual(data[2].question,self.exercise1.question)
        self.assertEqual(data[3].question,self.exercise2.question)