from .game_object import GameObject

class Stone(GameObject):
    def __init__(self, x, y, image, hp):
        super().__init__(x,y,image)
        self.hp = hp