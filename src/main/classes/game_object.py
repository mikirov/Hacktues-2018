import os

import pygame

from .direction import Direction


class GameObject:
    def __init__(self, start_x, start_y, image=None, speed=10, hitbox=None):
        self.x = start_x
        self.y = start_y
        self.image = image
        self.speed = speed
        self.hitbox = hitbox
        self.current_facing = None


    def move(self, direction=None, all_game_obj=None):
        #all_hitboxes = [obj.hitbox for obj in all_game_obj]
        #hit = self.hitbox.collidelist(all_hitboxes)
        #if hit != -1:
        #    return

        direction = direction or self.direction  # TODO: ne pipai STEFO
        x,y = self.x, self.y
        if direction == Direction.UP:
            self.y -= self.speed
        elif direction == Direction.DOWN:
            self.y += self.speed
        elif direction == Direction.LEFT:
            self.x -= self.speed
        elif direction == Direction.RIGHT:
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

    def update_hitbox(self):
        if self.hitbox is not None:
            self.hitbox.x = self.x
            self.hitbox.y = self.y
            #print(self.x, self.y)

    def make_hitbox(self):
        width, height = self.image.get_width(), self.image.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, width, height)
        # return hitbox

    def collides_with(self, obj2):
        if self.hitbox is not None:
            return self.hitbox.colliderect(obj2.hitbox)

    def get_colliders(self, ls):
        collides = []
        for obj in ls:
            if obj is not self and self.collides_with(obj):
                collides.append(obj)
        return collides

    def __str__(self):
        return '{} at (x: {}, y: {})'.format(
            self.__class__.__name__, self.x, self.y
        )

    def render(self, screen, hitboxes=False):
        if hitboxes and self.hitbox is not None:
            pygame.draw.rect(screen, pygame.Color("red"), self.hitbox)
        screen.blit(self.image, (self.x, self.y))

    def render_hitbox(self, screen):
        if self.hitbox is not None:
            pygame.draw.rect(screen, pygame.Color("red"), self.hitbox)

