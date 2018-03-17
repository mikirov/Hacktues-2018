import unittest
import pygame

from src.main.helpers.image_getter import get_image
from src.main.classes.game_object import GameObject
from src.main.classes.stone import Stone
from src.main.classes.player import Player
from src.main.classes.abilities import *
from src.main.classes.direction import Direction


class GameObjectTest(unittest.TestCase):
    def setUp(self):
        self.game_object = GameObject(100, 120, '/image/filepath', 10)

    def test_initial_values(self):
        self.assertEqual(100, self.game_object.x)
        self.assertEqual(120, self.game_object.y)
        #self.assertEqual('/image/filepath', self.game_object.image_filepath)
        self.assertEqual(10, self.game_object.speed)

    def test_move_up(self):
        self.game_object.move(Direction.UP)
        self.assertEqual(110, self.game_object.y)

    def test_move_down(self):
        self.game_object.move(Direction.DOWN)
        self.assertEqual(130, self.game_object.y)

    def test_move_right(self):
        self.game_object.move(Direction.RIGHT)
        self.assertEqual(110, self.game_object.x)

    def test_move_left(self):
        self.game_object.move(Direction.LEFT)
        self.assertEqual(90, self.game_object.x)


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 120, '/image/filepath', 10)

    def test_initial_values(self):
        self.assertEqual(100, self.player.x)
        self.assertEqual(120, self.player.y)
        #self.assertEqual('/image/filepath', self.player.image_filepath)
        self.assertEqual(10, self.player.speed)
        self.assertEqual(100, self.player.hp)

        
class AbilitiesTests(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 120, '/image/filepath', 10)

    def test_heal(self):
        self.player.heal()
        self.assertEqual(self.player.hp, 100 + self.player.heal_ability.amount)
        #self.assertEqual(self.player.heal_ability.current_cooldown, 5)

    def test_build(self):
        #building = Build(6)
        #print(building(self.player))
        self.assertEqual(isinstance(self.player.build(), GameObject), True)
        st = Stone(1, 3, "asd", 100)
        self.assertEqual(isinstance(st, Stone), True)


if __name__ == '__main__':
    unittest.main()

