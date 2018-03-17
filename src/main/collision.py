import pygame
import os


def make_hitbox(obj):
    #path = os.path.abspath("../resources/" + obj.image_filepath)
    path = os.path.join('src', 'resources', obj.image,)
    #print(path)
    surface = pygame.image.load(path)
    width, height = surface.get_width(), surface.get_height()
    obj.hitbox = pygame.Rect(obj.x, obj.y, width, height)
    #return hitbox

