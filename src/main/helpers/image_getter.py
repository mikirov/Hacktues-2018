import os
import pygame

image_library = {}


def get_image(path):
    image = image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        abs_path = os.path.abspath(canonicalized_path).replace('main', 'resources')
        image = pygame.image.load(abs_path)  # todo load ??
        image_library[path] = image
    return image
