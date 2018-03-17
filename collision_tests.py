import unittest
import pygame
import os

from src.main.classes.game_object import GameObject
from src.main.classes.player import Player
from src.main.classes.direction import Direction
from src.main.helpers.image_getter import get_image



class CollisionTests(unittest.TestCase):
    def setUp(self):
        self.game_object1 = GameObject(start_x=100, start_y=120,
                                       image=get_image('arrow.png'), speed=10)
        self.game_object2 = GameObject(start_x=100, start_y=120,
                                       image=get_image('player.png'), speed=10)
        self.game_object1.make_hitbox()
        self.game_object2.make_hitbox()
    def test_make_hitbox(self):
        #print(make_hitbox(self.game_object1))
        self.assertNotEqual(self.game_object1.hitbox, None)
        assert isinstance(self.game_object1.hitbox, pygame.Rect)
        self.assertNotEqual(self.game_object2.hitbox, None)
        assert isinstance(self.game_object2.hitbox, pygame.Rect)


    def test_surface_size(self):
        surface = pygame.image.load("src/resources/arrow.png")
        # print(surface.get_width(), surface.get_height())
        self.assertEquals(surface.get_width(), 16)
        self.assertEquals(surface.get_height(), 9)

    def test_no_collision(self):
        self.game_object2.move(Direction.RIGHT);
        self.assertTrue(self.game_object2.collides_with(self.game_object1))

    def test_move_hitbox(self):
        self.game_object1.move(Direction.UP)
        self.game_object2.move(Direction.UP)
        self.assertEquals(self.game_object1.x, self.game_object1.hitbox.x)
        self.assertEquals(self.game_object1.y, self.game_object1.hitbox.y)
        self.assertEquals(self.game_object2.x, self.game_object2.hitbox.x)
        self.assertEquals(self.game_object2.y, self.game_object2.hitbox.y)
        #print(self.game_object1.x, self.game_object1.y, self.game_object1.speed)
        #print(self.game_object1.hitbox)



if __name__ == '__main__':
    unittest.main()
