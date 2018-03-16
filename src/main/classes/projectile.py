from game_object import GameObject


class Projectile(GameObject):
    def __init__(self, start_x, start_y, damage=20):
        super().__init__(start_x, start_y)
        self.damage = damage

