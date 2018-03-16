import unittest

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.direction import Direction

class CollisionTests(unittest.TestCase):
    def setUp(self):
        self.game_object1 = GameObject(100, 120, '/image/filepath', 10)
        self.game_object2 = GameObject(80, 120, '/image/filepath', 10)
    def test_no_collision(self):
       self.game_object2.move(Direction.RIGHT);
       self.assertTrue(game_object2.collidesWith(game_object1))

if __name__ == '__main__':
    unittest.main()

