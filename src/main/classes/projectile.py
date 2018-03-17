from .game_object import GameObject
from .direction import Direction


class Projectile(GameObject):
    def __init__(self, start_x, start_y, direction,
                 image_filepath='projectile.png', speed=10, damage=40):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.direction = direction
        self.damage = damage

