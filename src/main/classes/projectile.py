from .game_object import GameObject


class Projectile(GameObject):
    def __init__(self, start_x, start_y, image_filepath=None, speed=10, damage=20):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.damage = damage
