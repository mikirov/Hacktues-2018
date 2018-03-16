import pygame

from pygame.sprite import Sprite

class Obstacle(Sprite):
    def __init___(self):
        super().__init__(self)
        self.rect = pygame.Rect(0, 0, 16, 16)
        self.image = pygame.image.load('src/resources/obstacle.png')
        self.obst_hp = 100
