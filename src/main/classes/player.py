from .direction import Direction
from .game_object import GameObject
from .abilities import Ability
import random

class Player(GameObject):
    def __init__(self, start_x, start_y, image_filepath=None, speed=10, hp=100):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.hp = hp
        self.current_facing = None
        self.ability = Ability("Heal", "passive", 5)
        self.ability.amount = random.randint(1,10)
        self.ability.func = ab.hp_change(self, self.hp+ab.amount)
    
    def move(self, direction):
        if direction == Direction.UP and self.y > 0:
            self.y -= self.speed
        elif direction == Direction.DOWN and self.y < 480:
            self.y += self.speed
        elif direction == Direction.LEFT and self.x > 0:
            self.x -= self.speed
        elif direction == Direction.RIGHT and self.x < 800:
            self.x += self.speed
        self.current_facing = direction

    def heal(self):
        ability()

    def shoot(self):
        pass 

