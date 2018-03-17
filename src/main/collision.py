import pygame
import os


def make_hitbox(obj):
    path = os.path.abspath("../resources/" + obj.image_filepath)
    surface = pygame.image.load(path)
    width, height = surface.get_width(), surface.get_height()
    hitbox = pygame.Rect(obj.x, obj.y, width, height)
    obj.hitbox = hitbox
