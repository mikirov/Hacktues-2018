from src.main.classes import game_object


class Projectile(game_object):
    def __init__(self, start_x, start_y, damage=20):
        super().__init__(start_x, start_y)
        self.damage = damage

