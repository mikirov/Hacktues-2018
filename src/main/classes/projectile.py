from .game_object import GameObject
from .direction import Direction


class Projectile(GameObject):
    def __init__(self, start_x, start_y, direction,
            image_filepath='projectile.png', speed=10, damage=20):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.direction = direction
        self.damage = damage

    def move(self, time_delta):
        if self.direction == Direction.UP:
            self.y -= self.speed * time_delta
        elif self.direction == Direction.DOWN:
            self.y += self.speed * time_delta
        elif self.direction == Direction.LEFT:
            self.x -= self.speed * time_delta
        elif self.direction == Direction.RIGHT:
            self.x += self.speed * time_delta

