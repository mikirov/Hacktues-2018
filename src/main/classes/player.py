import random
import math

from .direction import Direction
from .game_object import GameObject
from .projectile import Projectile
from .abilities import *


class Player(GameObject):
    def __init__(self, start_x, start_y, image=None, speed=10, hp=100, special_abilities=None):
        super().__init__(start_x, start_y, image, speed)
        self.hp = hp
        self.melee_dmg = 5
        self.current_facing = None
        self.heal_ability = Heal(5, random.randint(1, 10))
        self.build_ability = Build(6)
        self.special_abilities = special_abilities


    def heal(self):
        if self.heal_ability.current_cooldown == 0:
            self.heal_ability(self)
            self.heal_ability.current_cooldown = self.heal_ability.cool

    def shoot(self, projectile_image):
        # TODO: fix these arbitrary values
        projectile = Projectile(
            self.x + self.image.get_width() // 2,
            self.y + self.image.get_height() // 2,
            self.current_facing, projectile_image
        )
        return projectile

    def build(self, screen):  # todo not complete!!
        if self.build_ability.current_cooldown == 0:
            self.build_ability(self)
            self.build_ability.current_cooldown = self.build_ability.cool

    def hit(self, another_player):
        distance = math.sqrt(abs(self.x - another_player.x) ** 2 + abs(self.y - another_player.y) ** 2)
        if distance < 2.6:
            another_player.hp -= self.melee_dmg
