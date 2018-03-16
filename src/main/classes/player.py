from game_object import GameObject


class Player(GameObject):
    def __init__(self, start_x, start_y, speed=1):
        super().__init__(start_x, start_y)
        self.speed = 1

