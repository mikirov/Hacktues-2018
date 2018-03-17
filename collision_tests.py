import unittest
import pygame
import os

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.direction import Direction
from src.main.collision import make_hitbox
from src.main.helpers.image_getter import get_image


class CollisionTests(unittest.TestCase):
    def setUp(self):
        self.game_object1 = GameObject(start_x=100, start_y=120,
                                       image_filepath='arrow.png', speed=10)
        self.game_object2 = GameObject(start_x=100, start_y=120,
                                       image_filepath='player.png', speed=10)
        make_hitbox(self.game_object1)
        #make_hitbox(self.game_object2)
    def test_make_hitbox(self):
        #print(make_hitbox(self.game_object1))
        self.game_object2.hitbox = make_hitbox(self.game_object2)

    def test_surface_size(self):
        surface = pygame.image.load("src/resources/arrow.png")
        # print(surface.get_width(), surface.get_height())

    def test_no_collision(self):
        self.game_object2.move(Direction.RIGHT);
        self.assertTrue(self.game_object2.collides_with(self.game_object1))

    def test_move_hitbox(self):
        self.game_object1.move(0)
        #self.game_object1.hitbox.x = 4
        print(self.game_object1.x, self.game_object1.y, self.game_object1.speed)
        print(self.game_object1.hitbox.x, self.game_object1.hitbox.y)



if __name__ == '__main__':
    unittest.main()
