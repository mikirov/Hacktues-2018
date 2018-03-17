import pygame
from time import time

from evdev import InputDevice, categorize, ecodes
from classes import player
from classes import projectile
from classes.abilities import *
from helpers.image_getter import get_image
from controller_config import *
from classes.direction import Direction

# TODO SAY YOU HAVE KINDA FIXED THE IMPORTS

# set up gamepad
gamepad1 = InputDevice('/dev/input/event3')
# gamepad2 = InputDevice('/dev/input/event4')

# set up players
player1 = player.Player(50, 50, get_image('frontpl.png'))
player2 = player.Player(150, 50, get_image('frontpl.png'))

player1.special_ability = Build(5)
player2.special_ability = Heal(5, 20)

FONT_SIZE = 20

# main class
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.clock = None
        self.projectiles = []
        self.objects = []

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.SRCALPHA)
        self._running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.hp1 = self.font.render("HP:" + str(player1.hp), True, (0, 0, 0))
        self.hp2 = self.font.render("HP:" + str(player2.hp), True, (0, 0, 0))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.code == C1_BUTTON_DOWN:
            player1.move(Direction.DOWN)
            player1.image_filepath = 'frontpl.png'
        elif event.code == C1_BUTTON_UP:
            player1.move(Direction.UP)
            player1.image_filepath = 'backpl.png'
        elif event.code == C1_BUTTON_LEFT:
            player1.move(Direction.LEFT)
            player1.image_filepath = 'leftpl.png'
        elif event.code == C1_BUTTON_RIGHT:
            player1.move(Direction.RIGHT)
            player1.image_filepath = 'rightpl.png'
        elif event.code == C1_LEFT1:
            if player1.special_ability is Heal:
                player1.special_ability()
        elif event.code == C1_LEFT2:
            player1.hit()  # incomplete
        elif event.code == C1_RIGHT1:
            projectile = player1.shoot()
            self.projectiles.append(projectile)
            self.objects.append(projectile)
        elif event.code == C1_RIGHT2:
            if player1.special_ability is Build:
                self.objects.append(player1.build(player1)) # todo what da Fu

        # player 2 buttons :

        elif event.code == C2_BUTTON_DOWN:
            player2.move(Direction.DOWN)
        elif event.code == C2_BUTTON_UP:
            player2.move(Direction.UP)
        elif event.code == C2_BUTTON_LEFT:
            player2.move(Direction.LEFT)
        elif event.code == C2_BUTTON_RIGHT:
            player2.move(Direction.RIGHT)

        elif event.code == C2_LEFT1:
            pass
        elif event.code == C2_LEFT2:
            pass
        elif event.code == C2_RIGHT1:
            pass
        elif event.code == C2_RIGHT2:
            pass

    def loop(self):
        self.clock.tick(60)

    def render(self):
        for current_object in self.objects:
            current_object.render(self.screen)

        pygame.display.flip()

    @staticmethod
    def cleanup():
        pygame.quit()

    def execute(self):
        self.on_init()
        current_time = time()
        self.screen.fill((255, 255, 255))
        self.render()
        while self._running:
            previous_time = current_time
            current_time = time()
            time_delta = current_time - previous_time

            to_remove = set()
            for i in range(0, len(self.projectiles)):
                current_projectile = self.projectiles[i]
                current_projectile.move(time_delta)
                if not 0 <= current_projectile.x <= self.width or not 0 <= current_projectile.y <= self.height:
                    to_remove.add(i)

            self.projectiles = list(
                filter(lambda proj: self.projectiles.index(proj) not in to_remove, self.projectiles)
            )

            event1 = gamepad1.read_one()
            if event1 is not None and event1.type == ecodes.EV_KEY:
                self.on_event(event1)
            self.loop()
            self.render()
            self.screen.fill((255, 255, 255))
        self.cleanup()

        """
        self.screen.fill((255, 255, 255))
        self.render()
        for event1, event2 in zip(gamepad1.read_loop(), gamepad2.read_loop()):
            if not self._running:
                break

            if event1.type == ecodes.EV_KEY:
                self.on_event(event1)
            if event2.type == ecodes.EV_KEY:
                print(event2)
                self.on_event(event2)
            self.loop()
            self.render()
            self.screen.fill((255, 255, 255))
        self.cleanup()
        """


if __name__ == "__main__":
    theApp = App()
    theApp.execute()
