from classes.game_object import GameObject
from classes.direction import Direction


class Projectile(GameObject):
    def __init__(self, start_x, start_y, player, direction,
                 image='fireball.png', speed=10, damage=40):
        super().__init__(start_x, start_y, image, speed)
        self.player = player
        self.direction = direction
        self.damage = damage

