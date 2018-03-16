import unittest

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.direction import Direction

class CollisionTests(unittest.TestCase):
    def setUp(self):
        self.game_object1 = GameObject(100, 120, '/image/filepath', 10)
        self.game_object2 = GameObject(20, 120, '/image/filepath', 10)
    def test_no_collision(self):
        pass

if __name__ == '__main__':
    unittest.main()

