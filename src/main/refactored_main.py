from time import time
from select import select

import evdev
import pygame

from helpers.image_getter import get_image
from classes.player import Player
from classes.stone import Stone
from classes.direction import Direction
from config.controller_config import *
from config.game_config import *


class Game:
    def __init__(self):
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self._running = False
        self.devices = [gamepad1, gamepad2]
        self.projectiles = []
        self.player1 = Player(*PLAYER_1_STARTING_COORDS, get_image(PLAYER_1_IMAGE), hp=STARTING_HP)
        self.player1.hitbox = pygame.Rect(self.player1.x, self.player1.y, 64, 64)
        self.player2 = Player(*PLAYER_2_STARTING_COORDS, get_image(PLAYER_2_IMAGE), hp=STARTING_HP)
        self.player2.hitbox = pygame.Rect(self.player2.x, self.player2.y, 64, 64)
        self.game_objects = [self.player1, self.player2]
        self.events = {
            C1_BUTTON_DOWN: False,
            C1_BUTTON_UP: False,
            C1_BUTTON_LEFT: False,
            C1_BUTTON_RIGHT: False,
            C1_LEFT1: False,
            C1_LEFT2: False,
            C1_RIGHT1: False,
            C1_RIGHT2: False,

            C2_BUTTON_DOWN * 2: False,
            C2_BUTTON_UP * 2: False,
            C2_BUTTON_LEFT * 2: False,
            C2_BUTTON_RIGHT * 2: False,
            C2_LEFT1 * 2: False,
            C2_LEFT2 * 2: False,
            C2_RIGHT1 * 2: False,
            C2_RIGHT2 * 2: False,
        }

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self._running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

    def on_event(self, event, current_player):
        if event.code == EXIT_BUTTON:
            self._running = False
        else:
            if event.value == 1:
                self.events[event.code * current_player] = True
            else:
                self.events[event.code * current_player] = False

    def process_input(self):
        # Player 1
        if self.events[C1_BUTTON_DOWN]:
            self.player1.move(Direction.DOWN, self.game_objects)
        if self.events[C1_BUTTON_UP]:
            self.player1.move(Direction.UP, self.game_objects)
        if self.events[C1_BUTTON_LEFT]:
            self.player1.move(Direction.LEFT, self.game_objects)
        if self.events[C1_BUTTON_RIGHT]:
            self.player1.move(Direction.RIGHT, self.game_objects)
        if self.events[C1_LEFT1]:
            self.player1.heal()
        if self.events[C1_LEFT2]:
            self.player1.hit(self.player2)
        if self.events[C1_RIGHT1]:
            current_time = time()
            if current_time - self.player1.last_projectile_fired_at >= COOLDOWN:
                projectile = self.player1.shoot(get_image(PROJECTILE_IMAGE))
                self.projectiles.append(projectile)
                self.player1.last_projectile_fired_at = current_time
        if self.events[C1_RIGHT2]:
            stone = self.player1.build()
            stone.image = get_image(stone.image)
            stone.make_hitbox()
            self.game_objects.append(stone)

        # Player 2
        if self.events[C2_BUTTON_DOWN * 2]:
            self.player2.move(Direction.DOWN, self.game_objects)
        if self.events[C2_BUTTON_UP * 2]:
            self.player2.move(Direction.UP, self.game_objects)
        if self.events[C2_BUTTON_LEFT * 2]:
            self.player2.move(Direction.LEFT, self.game_objects)
        if self.events[C2_BUTTON_RIGHT * 2]:
            self.player2.move(Direction.RIGHT, self.game_objects)
        if self.events[C2_LEFT1 * 2]:
            self.player2.heal()
        if self.events[C2_LEFT2 * 2]:
            self.player2.hit(self.player1)
        if self.events[C2_RIGHT1 * 2]:
            current_time = time()
            if current_time - self.player2.last_projectile_fired_at >= COOLDOWN:
                projectile = self.player2.shoot(get_image(PROJECTILE_IMAGE))
                self.projectiles.append(projectile)
                self.player2.last_projectile_fired_at = current_time
        if self.events[C2_RIGHT2 * 2]:
            stone = self.player2.build()
            stone.image = get_image(stone.image)
            stone.make_hitbox()
            self.game_objects.append(stone)

    def loop(self):
        to_remove = set()
        for current_proj in self.projectiles:
            current_proj.move()
            collisions = current_proj.collides_any(self.game_objects)
            if collisions:  # if the projectile collides
                to_remove.add(current_proj)
                for obj in collisions:
                    if isinstance(obj, Stone) or isinstance(obj, Player):
                        obj.hp -= current_proj.damage
                        if obj.hp <= 0:
                            to_remove.add(obj)

        self.projectiles = list(
            filter(lambda proj: proj not in to_remove, self.projectiles)
        )
        self.game_objects = list(
            filter(lambda obj: obj not in to_remove, self.game_objects)
        )
        
        # Game over
        if self.player1.hp <= 0 or self.player2.hp <= 0:
            self.reset()
        self.clock.tick(20)

    def render(self):
        self.screen.fill(WHITE)
        self.screen.blit(get_image(BACKGROND_IMAGE), (0, 0))

        # HP
        hp1 = self.font.render('HP:' + str(self.player1.hp), True, (0, 0, 0))
        hp2 = self.font.render('HP:' + str(self.player2.hp), True, (0, 0, 0))
        self.screen.blit(hp1, HP1_RENDER_COORDS)
        self.screen.blit(hp2, HP2_RENDER_COORDS)

        # Game objects
        for obj in self.game_objects:
            if obj is None or obj == self.player1 or obj == self.player2:
                continue
            obj.render(self.screen)

        # Projectiles
        for projectile in self.projectiles:
            projectile.render(self.screen)

        # Players
        self.player1.rect = pygame.Rect(
            self.player1.frame * 64, 64 * self.player1.current_facing.value,
            64, 64,
        )
        self.screen.blit(
            self.player1.image, (self.player1.x, self.player1.y),
            self.player1.rect,
        )
        self.player1.frame += 1
        if self.player1.frame >= 9:
            self.player1.frame = 0
        self.player2.rect = pygame.Rect(
            self.player2.frame * 64, 64 * self.player2.current_facing.value,
            64, 64,
        )
        self.screen.blit(
            self.player2.image, (self.player2.x, self.player2.y),
            self.player2.rect,
        )
        self.player2.frame += 1
        if self.player2.frame >= 9:
            self.player2.frame = 0
        pygame.display.flip()

    def execute(self):
        self.on_init()
        self.screen.fill(WHITE)
        self.render()

        devs = {dev.fd: dev for dev in devices if dev is not None}
        while self._running:
            r, w, x = select(devs, [], [], 1/FRAMERATE)
            for fd in r:
                for event in devs[fd].read():
                    if event.type == evdev.ecodes.EV_KEY:
                        player = 1 if devs[fd] is gamepad1 else 2
                        if event.type == evdev.ecodes.EV_KEY:
                            self.on_event(event, player)
            self.process_input()
            self.loop()
            self.render()
        self.cleanup()

    @staticmethod
    def cleanup():
        pygame.quit()

    def reset(self):
        self.projectiles = []
        self.game_objects = [self.player1, self.player2]
        self.player1.hp, self.player2.hp = STARTING_HP, STARTING_HP
        self.player1.x, self.player1.y = PLAYER_1_STARTING_COORDS
        self.player1.hitbox = pygame.Rect(*PLAYER_1_STARTING_COORDS, 64, 64)
        self.player2.x, self.player2.y = PLAYER_2_STARTING_COORDS
        self.player2.hitbox = pygame.Rect(*PLAYER_2_STARTING_COORDS, 64, 64)


def find_device(name):
    for dev in devices:
        if name in dev.name:
            return dev


def main():
    global devices, gamepad1, gamepad2

    devices = [evdev.InputDevice(dev) for dev in evdev.list_devices()]
    gamepad1 = find_device(GAMEPAD_NAME_1)
    gamepad2 = find_device(GAMEPAD_NAME_2)

    game = Game()
    game.execute()


if __name__ == '__main__':
    main()

