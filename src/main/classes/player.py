from game_object import GameObject


class Player(GameObject):
    def __init__(self, start_x, start_y, hp=100):
        super().__init__(start_x, start_y)
        self.hp = hp 

