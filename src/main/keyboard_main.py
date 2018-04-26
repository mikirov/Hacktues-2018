from time import time
from select import select

import evdev
import pygame

from helpers.image_getter import get_image
from helpers.device_finder import find_device
from classes.player import Player
from classes.stone import Stone
from classes.abilities import Build
from classes.direction import Direction
from config.keyboard_config import *
from config.game_config import *


class Game:
    def __init__(self, debug=False):
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self._running = False
        self._debug = debug
        self.devices = [gamepad1, gamepad2]
        self.projectiles = []
        self.player1 = Player(
            *PLAYER_1_STARTING_COORDS, get_image(PLAYER_1_IMAGE),
            speed=PLAYER_SPEED, hp=MAX_HP,
        )
        self.player1.update_hitbox()
        self.player1.add_animation(64, 64, 9)
        self.player2 = Player(
            *PLAYER_2_STARTING_COORDS, get_image(PLAYER_2_IMAGE),
            speed=PLAYER_SPEED, hp=MAX_HP,
        )
        self.player2.update_hitbox()
        self.player2.add_animation(64, 64, 9)
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

            C2_BUTTON_DOWN: False,
            C2_BUTTON_UP: False,
            C2_BUTTON_LEFT: False,
            C2_BUTTON_RIGHT: False,
            C2_LEFT1: False,
            C2_LEFT2: False,
            C2_RIGHT1: False,
            C2_RIGHT2: False,
        }

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self._running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

    def on_event(self, event):
        if event.code == EXIT_BUTTON:
            self._running = False
        else:
            if event.value == 0:
                self.events[event.code] = False
            else:
                self.events[event.code] = True

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
        if self.events[C1_RIGHT2]:
            current_time = time()
            if current_time - self.player1.last_projectile_fired_at >= COOLDOWN:
                projectile = self.player1.shoot(get_image(PROJECTILE_IMAGE))
                self.projectiles.append(projectile)
                self.player1.last_projectile_fired_at = current_time
        if self.events[C1_RIGHT1]:
            current_time = time()
            if current_time - self.player1.last_wall_built_at >= COOLDOWN:
                stone = self.player1.build()
                if stone is not None:
                    stone.image = get_image(stone.image)
                    stone.make_hitbox()
                    if self.player1.collides_with(stone):
                        return
                    self.game_objects.append(stone)
                    self.player1.last_wall_built_at = current_time

        # Player 2
        if self.events[C2_BUTTON_DOWN]:
            self.player2.move(Direction.DOWN, self.game_objects)
        if self.events[C2_BUTTON_UP]:
            self.player2.move(Direction.UP, self.game_objects)
        if self.events[C2_BUTTON_LEFT]:
            self.player2.move(Direction.LEFT, self.game_objects)
        if self.events[C2_BUTTON_RIGHT]:
            self.player2.move(Direction.RIGHT, self.game_objects)
        if self.events[C2_LEFT1]:
            self.player2.heal()
        if self.events[C2_LEFT2]:
            self.player2.hit(self.player1)
        if self.events[C2_RIGHT2]:
            current_time = time()
            if current_time - self.player2.last_projectile_fired_at >= COOLDOWN:
                projectile = self.player2.shoot(get_image(PROJECTILE_IMAGE))
                self.projectiles.append(projectile)
                self.player2.last_projectile_fired_at = current_time
        if self.events[C2_RIGHT1]:
            current_time = time()
            if current_time - self.player2.last_wall_built_at >= COOLDOWN:
                stone = self.player2.build()
                if stone is not None:
                    stone.image = get_image(stone.image)
                    stone.make_hitbox()
                    if self.player2.collides_with(stone):
                        return
                    self.game_objects.append(stone)
                    self.player2.last_wall_built_at = current_time
                        

    def loop(self):
        to_remove = set()
        for current_proj in self.projectiles:
            current_proj.move(all_game_obj=self.game_objects)
            collisions = current_proj.get_colliders(self.game_objects)
            if collisions:  # if the projectile collides
                to_remove.add(current_proj)
                for obj in collisions:
                    if isinstance(obj, Stone) or isinstance(obj, Player):
                        obj.hp -= current_proj.damage
                        if obj.hp <= 0:
                            if isinstance(obj, Stone):
                                Build.grid[obj.grid_y][obj.grid_x]
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
            obj.render(self.screen, self._debug)

        # Projectiles
        for projectile in self.projectiles:
            projectile.render(self.screen, self._debug)

        # Players
        self.player1.base_animation.play(self.screen)
        self.player2.base_animation.play(self.screen)
        if self._debug:
            self.player1.render_hitbox(self.screen)
            self.player2.render_hitbox(self.screen)
        pygame.display.flip()

    def execute(self):
        self.on_init()
        self.screen.fill(WHITE)
        self.render()

        devs = {dev.fd: dev for dev in self.devices if dev is not None}
        while self._running:
            r, w, x = select(devs, [], [], 1/FRAMERATE)
            for fd in r:
                for event in devs[fd].read():
                    if event.type == evdev.ecodes.EV_KEY or event.type == 3:
                        self.on_event(event)
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
        self.player1.hp, self.player2.hp = MAX_HP, MAX_HP
        self.player1.x, self.player1.y = PLAYER_1_STARTING_COORDS
        self.player1.update_hitbox()
        self.player2.x, self.player2.y = PLAYER_2_STARTING_COORDS
        self.player2.update_hitbox()


def main():
    global gamepad1, gamepad2

    gamepad1 = gamepad2 = keyboard

    game = Game() # give True to enable hitbox drawing
    game.execute()  


if __name__ == '__main__':
    main()

