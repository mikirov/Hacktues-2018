import unittest

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.direction import Direction


class DirectionTests(unittest.TestCase):
    def setUp(self):
        self.starting_x = 100
        self.player = Player(self.starting_x, 120, '/image/filepath', 10)

    def test_direction(self):
        self.player.move(Direction.RIGHT)
        self.assertEqual(self.player.x, self.starting_x + self.player.speed)


if __name__ == '__main__':
    unittest.main()
