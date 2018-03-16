from src.main.classes import game_object, projectile


class Player(game_object.GameObject):
    def __init__(self, start_x, start_y,img, speed, hp=100):
        super().__init__(start_x, start_y, img, speed)
        self.hp = hp

    def shoot(self):
        pass 

