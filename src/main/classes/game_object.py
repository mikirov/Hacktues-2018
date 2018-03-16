from .direction import Direction

class GameObject:
    def __init__(self, start_x, start_y, image_filepath=None, speed=10):
        self.x = start_x
        self.y = start_y
        self.image_filepath = image_filepath
        self.speed = speed

    def move(self, direction):
        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
            self.x += self.speed

    def __str__(self):
        return '{} at (x: {}, y: {})'.format(
            self.__class__.__name__, self.x, self.y
        )

