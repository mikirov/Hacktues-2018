import unittest

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.direction import Direction
from src.main.collision import make_hitbox


class CollisionTests(unittest.TestCase):
    def setUp(self):
        self.game_object1 = GameObject(start_x=100, start_y=120,
                                       image_filepath='src/main/resources/player.png', speed=10)
        self.game_object2 = GameObject(start_x=100, start_y=120,
                                       image_filepath='src/main/resources/player2.png', speed=10)
        make_hitbox(self.game_object1)
        make_hitbox(self.game_object2)

    def test_no_collision(self):
        self.game_object2.move(Direction.RIGHT);
        self.assertTrue(self.game_object2.collides_with(self.game_object1))


if __name__ == '__main__':
    unittest.main()
