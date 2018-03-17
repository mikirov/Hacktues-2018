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
        self.melee_dmg = 6
        self.current_facing = None
        self.heal_ability = Heal(5, random.randint(1, 10))
        self.build_ability = Build(6)

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
        if self.hitbox is not None:
            self.hitbox.x = self.x
            self.hitbox.y = self.y  # todo wtf??

    def heal(self):
        if self.heal_ability.current_cooldown == 0:
            self.heal_ability(self)
            self.heal_ability.current_cooldown = self.heal_ability.cool

    def shoot(self):
        # TODO: fix these arbitrary values
        projectile = Projectile(
            self.x + 10, self.y - 10,
            Direction.UP, 'projectile.png'
        )
        return projectile

    def build(self, screen):
        if self.build_ability.current_cooldown == 0:
            self.build_ability(self)
            self.build_ability.current_cooldown = self.build_ability.cool

    def hit(self, another_player):
        distance = math.sqrt(abs(self.x - self.x) ** 2 + abs(self.y - self.x) ** 2)
        if distance < 5:
            another_player.hp -= self.melee_dmg
