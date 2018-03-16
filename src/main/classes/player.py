from .game_object import GameObject


class Player(GameObject):
    def __init__(self, start_x, start_y, image_filepath=None, speed=10, hp=100):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.hp = hp
    
    def move(self, direction):
        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
            self.x += self.speed

    def shoot(self):
        pass 

