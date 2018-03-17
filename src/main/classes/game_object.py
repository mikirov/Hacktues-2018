from .direction import Direction
import pygame

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 800

class GameObject:
    def __init__(self, start_x, start_y, image_filepath=None, speed=10):
        self.x = start_x
        self.y = start_y
        self.image_filepath = image_filepath
        self.speed = speed

    def move(self, direction):
        if direction == Direction.UP and self.y > 0:
            self.y -= self.speed
        elif direction == Direction.DOWN and self.y < SCREEN_HEIGHT:
            self.y += self.speed
        elif direction == Direction.LEFT and self.x > 0:
            self.x -= self.speed
        elif direction == Direction.RIGHT and self.x < SCREEN_WIDTH:
            self.x += self.speed

    def collides_with(self, obj2):
        if "hitbox" in dir(self):
            return self.hitbox.colliderect(obj2.hitbox) # todo

    def __str__(self):
        return '{} at (x: {}, y: {})'.format(
            self.__class__.__name__, self.x, self.y
        )
