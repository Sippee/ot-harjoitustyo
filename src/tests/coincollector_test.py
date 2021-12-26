import unittest
from collectinggame.coincollector import Coin, Collector, Window, main_game

class TestCoin(unittest.TestCase):
    def setUp(self):
        self.game_window = Window(500,500)
        self.coin = Coin(100,100,self.game_window)

    def test_coin_stats(self):
        self.assertEqual(self.coin.x_coordinate, 100)
        self.assertEqual(self.coin.y_coordinate, 100)
        self.assertEqual(self.coin.height, 20)
        self.assertEqual(self.coin.width, 20)
        self.assertEqual(self.coin.window, self.game_window)
        self.assertEqual(self.coin.draw(), None)

class TestCollector(unittest.TestCase):
    def setUp(self):
        self.game_window = Window(500,500)
        self.collector = Collector(100,100,self.game_window)

    def test_colector_stats(self):
        self.assertEqual(self.collector.x_coordinate, 100)
        self.assertEqual(self.collector.y_coordinate, 100)
        self.assertEqual(self.collector.height, 40)
        self.assertEqual(self.collector.width, 40)
        self.assertEqual(self.collector.speed, 5)
        self.assertEqual(self.collector.window, self.game_window)
        self.assertEqual(self.collector.draw(), None)