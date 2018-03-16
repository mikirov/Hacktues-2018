import unittest

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.abilities import Ability 


class GameObjectTest(unittest.TestCase):
    def setUp(self):
        self.game_object = GameObject(100, 120, '/image/filepath', 10)

    def test_initial_values(self):
        self.assertEqual(100, self.game_object.x)
        self.assertEqual(120, self.game_object.y)
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


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 120, '/image/filepath', 10)

    def test_initial_values(self):
        self.assertEqual(100, self.player.x)
        self.assertEqual(120, self.player.y)
        self.assertEqual('/image/filepath', self.player.image_filepath)
        self.assertEqual(10, self.player.speed)
        self.assertEqual(100, self.player.hp)

        
class AbilitiesTests(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 120, '/image/filepath', 10)

    def test_heal(self):
        ability = Ability('Heal', 'stats_based', 3)
        ability.heal_amount = 20
        ability.hp_change(self.player, self.player.hp + ability.heal_amount)
        self.assertEqual(self.player.hp, 120)

class DirectionTests(unittest.TestCase):
    def setUp(self):
        self.starting_x = 100
        self.player = Player(self.starting_x, 120, '/image/filepath', 10)

    def test_direction(self):
        self.player.move(Direction.RIGHT);
        assertEqual(self.player.x == self.starting_x + self.player.speed)

if __name__ == '__main__':
    unittest.main()

