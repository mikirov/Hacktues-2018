from .direction import Direction
import os
import pygame

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 800


class GameObject:
    def __init__(self, start_x, start_y, image=None, speed=10, hitbox=None):
        self.x = start_x
        self.y = start_y
        self.image = image
        self.speed = speed
        self.hitbox = None
        self.current_facing = None


    def move(self, direction=None):
        direction = direction or self.current_facing
        if direction == Direction.UP and self.y > 0:
            self.y -= self.speed
        elif direction == Direction.DOWN and self.y < SCREEN_HEIGHT:
            self.y += self.speed
        elif direction == Direction.LEFT and self.x > 0:
            self.x -= self.speed
        elif direction == Direction.RIGHT and self.x < SCREEN_WIDTH:
            self.x += self.speed
        self.current_facing = direction
        if self.hitbox is not None:
            self.hitbox.x = self.x
            self.hitbox.y = self.y  # todo wtf??

    def make_hitbox(self):
        # path = os.path.abspath("../resources/" + obj.image_filepath)
        path = os.path.join('src', 'resources', self.image )
        # print(path)
        surface = pygame.image.load(path)
        width, height = surface.get_width(), surface.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, width, height)
        # return hitbox

    def collides_with(self, obj2):
        if self.hitbox is not None:
            return self.hitbox.colliderect(obj2.hitbox)  # todo

    def __str__(self):
        return '{} at (x: {}, y: {})'.format(
            self.__class__.__name__, self.x, self.y
        )

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
