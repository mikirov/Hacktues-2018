import random
import math

from .direction import Direction
from .game_object import GameObject
from .projectile import Projectile
from .abilities import *


class Player(GameObject):
    def __init__(self, start_x, start_y, image=None, speed=10, hp=100, special_abilities=None, frame = 0):
        super().__init__(start_x, start_y, image, speed)
        self.hp = hp
        self.melee_dmg = 30
        self.current_facing = Direction.DOWN
        self.heal_ability = Heal(5, random.randint(1, 10))
        self.build_ability = Build(6, 50)
        self.special_abilities = special_abilities
        self.frame = frame
        self.last_projectile_fired_at = 0  # time since the epoch

    def heal(self):
        #if self.heal_ability.current_cooldown == 0:
        self.heal_ability(self)
            #self.heal_ability.current_cooldown = self.heal_ability.cool

    def shoot(self, projectile_image):
        projectile = Projectile(
            self.x + self.hitbox.width // 2,
            self.y + self.hitbox.height // 2,
            self, self.current_facing, projectile_image
        )
        projectile.make_hitbox()
        return projectile

    def build(self):  # todo not complete!!
        #if self.build_ability.current_cooldown == 0:
            #self.build_ability.current_cooldown = self.build_ability.cool
        return self.build_ability(self)

    def hit(self, another_player):
        distance = math.sqrt(abs(self.x - another_player.x) ** 2 + abs(self.y - another_player.y) ** 2)
        if distance < 26:
            another_player.hp -= self.melee_dmg

