from game_object import GameObject


class Player(GameObject):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)

