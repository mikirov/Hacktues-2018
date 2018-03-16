import random
import math

from .direction import Direction
from .game_object import GameObject
from .projectile import Projectile
from .abilities import *

class Player(GameObject):
    def __init__(self, start_x, start_y, image_filepath=None, speed=10, hp=100):
        super().__init__(start_x, start_y, image_filepath, speed)
        self.hp = hp
        self.mele_dmg = 6
        self.current_facing = None
        self.heal_ab = Heal(5, random.randint(1,10))
        self.build_ab = Build(6)
        self.image_width = None
        self.image_height = None
    
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
        if "hitbox" in dir(self):
            self.hitbox.x = self.x
            self.hitbox.y = self.y

    def heal(self):
        if self.heal_ab.current_cooldown == 0:
            self.heal_ab(self)
            self.heal_ab.current_cooldown = self.heal_ab.cool

    def shoot(self):
        print(self.current_facing)
        # TODO: fix these arbitrary values
        projectile = Projectile(
            self.x + self.image_width // 2, self.y - self.image_height // 2,
            self.current_facing, 'projectile.png'
        )
        return projectile

    def build(self, screen):
        if self.build_ab.current_cooldown == 0:
            self.build_ab(self)
            self.build_ab.current_cooldown = self.build_ab.cool

    def hit(self, player2):
        dist = math.sqrt(abs(self.x-self.x)**2 + abs(self.y-self.x)**2)
        if dist < 5:
            player2.hp -= self.mele_dmg
