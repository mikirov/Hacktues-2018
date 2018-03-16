import pygame

class Obsticle(pygame.sprite.Sprite):
    def __init___(self):
        self.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0, 16, 16)
        self.image = pygame.image.load('src/resources/player.png')
        self.obst_hp = 100
