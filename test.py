import unittest

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.abilities import Ability 


class GameObjectTest(unittest.TestCase):
    def setUp(self):
        self.game_object = GameObject(100, 120, 30, 20, '/image/filepath', 10)

    def test_initial_values(self):
        self.assertEqual(100, self.game_object.x)
        self.assertEqual(120, self.game_object.y)
        self.assertEqual(30, self.game_object.image_width)
        self.assertEqual(20, self.game_object.image_height)
        self.assertEqual('/image/filepath', self.game_object.image_filepath)
        self.assertEqual(10, self.game_object.speed)

    def test_move_up(self):
        self.game_object.move_up()
        self.assertEqual(110, self.game_object.y)

    def test_move_down(self):
        self.game_object.move_down()
        self.assertEqual(130, self.game_object.y)

    def test_move_right(self):
        self.game_object.move_right()
        self.assertEqual(110, self.game_object.x)

    def test_move_left(self):
        self.game_object.move_left()
        self.assertEqual(90, self.game_object.x)

"""
class AbilitiesTests(unittest.TestCase):
    def test_heal(self):
        pl = player.Player(3, 4, 20, 20, '', 5)
        ab = abilities.Ability("Heal", "stats_based", 3)
        ab.heal_amount = 20
        ab.hp_change(pl, pl.hp+ab.heal_amount)
        self.assertEqual(pl.hp, 120)
"""

if __name__ == '__main__':
    unittest.main()

