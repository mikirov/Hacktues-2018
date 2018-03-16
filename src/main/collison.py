import pygame
from .helpers import image_getter

def make_hitbox(obj):
    surface = image_getter.get_image(obj.image_filepath)
    width, height = surface.get_width(), surface.get_height()
    hitbox = pygame.Rect(obj.x, obj.y, width, height)
    obj.hitbox = hitbox

def collides(obj1, obj2):
    return obj1.hitbox.colliderect(obj2.hitbox)