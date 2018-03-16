from .direction import Direction
from .game_object import GameObject
from .abilities import Ability
import random

class Player(GameObject):
    def __init__(self, start_x, start_y, image_filepath=None, speed=10, hp=100):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.hp = hp
        self.current_facing = None
        self.heal_ab = Ability("Heal", "passive", 5)
        self.heal_ab.amount = random.randint(1,10)
        self.heal_ab.func = self.heal_ab.hp_change(self, self.hp+self.heal_ab.amount)
    
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
        if self.heal_ab.current_cooldown == 0:
            self.heal_ab()
            self.heal_ab.current_cooldown = self.heal_ab.cool

    def shoot(self):
        pass 

