from src.main.helpers.image_getter import get_image
from .direction import Direction

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 800


class GameObject:
    def __init__(self, start_x, start_y, image_filepath=None, speed=10, hitbox=None):
        self.x = start_x
        self.y = start_y
        self.image_filepath = image_filepath
        self.speed = speed
        self.hitbox = None


    def move(self, direction):
        if direction == Direction.UP and self.y > 0:
            self.y -= self.speed
        elif direction == Direction.DOWN and self.y < SCREEN_HEIGHT:
            self.y += self.speed
        elif direction == Direction.LEFT and self.x > 0:
            self.x -= self.speed
        elif direction == Direction.RIGHT and self.x < SCREEN_WIDTH:
            self.x += self.speed
        if self.hitbox is not None:
            print("Moving hitbox")
            self.hitbox.x = self.x
            self.hitbox.y = self.y  # todo wtf??

    def collides_with(self, obj2):
        if self.hitbox is not None:
            return self.hitbox.colliderect(obj2.hitbox)  # todo

    def __str__(self):
        return '{} at (x: {}, y: {})'.format(
            self.__class__.__name__, self.x, self.y
        )

    def render(self, screen):
        screen.blit(get_image(self.image_filepath), (self.x, self.y))
