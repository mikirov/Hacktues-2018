import pygame
from helpers.image_getter import *

def make_hitbox(obj):
    surface = get_image(obj.image_filepath)
    width, height = surface.get_width(), surface.get_height()
    hitbox = pygame.Rect(obj.x, obj.y, width, height)
    obj.hitbox = hitbox

