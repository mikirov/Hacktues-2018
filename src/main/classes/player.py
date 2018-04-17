import random
import math

from .direction import Direction
from .game_object import GameObject
from .projectile import Projectile
from .abilities import *

SCREEN_HEIGHT = 350
SCREEN_WIDTH = 620

class Player(GameObject):
    def __init__(self, start_x, start_y, image=None, speed=5, hp=100, special_abilities=None, frame = 0):
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
          #  self.heal_ability.current_cooldown = self.heal_ability.cool

    def shoot(self, projectile_image):
        base_x = self.x + self.hitbox.width // 2
        base_y = self.y + self.hitbox.height // 2
        offset = 35
        if self.current_facing == Direction.UP:
            base_y -= self.hitbox.height
        if self.current_facing == Direction.DOWN:
            base_y += self.hitbox.height - offset
        if self.current_facing == Direction.LEFT:
            base_x -= self.hitbox.width
        if self.current_facing == Direction.RIGHT:
            base_x += self.hitbox.width - offset
        projectile = Projectile(
            base_x,
            base_y,
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


    def move(self, direction=None, all_game_obj=None):
        #all_hitboxes = [obj.hitbox for obj in all_game_obj]
        #hit = self.hitbox.collidelist(all_hitboxes)
        #if hit != -1:
        #    return

        direction = direction or self.direction  # TODO: ne pipai STEFO
        x,y = self.x, self.y
        if direction == Direction.UP and self.y > 0:
            self.y -= self.speed
        elif direction == Direction.DOWN and self.y  + self.hitbox.height < SCREEN_HEIGHT:
            self.y += self.speed
        elif direction == Direction.LEFT and self.x > 0:
            self.x -= self.speed
        elif direction == Direction.RIGHT and self.x + self.hitbox.width < SCREEN_WIDTH:
            self.x += self.speed
        self.current_facing = direction
        self.update_hitbox()

            #all_hitboxes = [obj.hitbox for obj in all_game_obj]
           # ind = self.hitbox.collidelist(all_hitboxes)
            #if ind != -1:
             #   self.x = x
              #  self.y = y
               # self.hitbox.x = x
                #self.hitbox.y = y