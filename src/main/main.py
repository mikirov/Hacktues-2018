import pygame
from time import time

from evdev import InputDevice, categorize, ecodes
from classes import player
from classes import projectile
from classes.abilities import *
from helpers.image_getter import get_image
from controller_config import *
from classes.direction import Direction

# set up gamepad
gamepad1 = InputDevice('/dev/input/event4')
gamepad2 = InputDevice('/dev/input/event3')

# set up players
player1 = player.Player(50, 50, get_image('mage-only.png'))
player1.make_hitbox()
player2 = player.Player(150, 50, get_image('mage-only.png'))
player2.make_hitbox()

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
        self.objects = [player1, player2]

    def on_init(self):
        pygame.init()
        # self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode(self.size, pygame.SRCALPHA)
        self._running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

    def on_event(self, event, player):
        if event.type == pygame.QUIT:
            self._running = False
        elif player == 1:
            if event.code == C1_BUTTON_DOWN:
                player1.move(Direction.DOWN)
            elif event.code == C1_BUTTON_UP:
                player1.move(Direction.UP)
            elif event.code == C1_BUTTON_LEFT:
                player1.move(Direction.LEFT)
            elif event.code == C1_BUTTON_RIGHT:
                player1.move(Direction.RIGHT)
            elif event.code == C1_LEFT1:
                player1.heal_ability()
            elif event.code == C1_LEFT2:
                player1.hit(player2)  # incomplete
            elif event.code == C1_RIGHT1:
                projectile = player1.shoot(get_image('projectile.png'))
                self.projectiles.append(projectile)
            elif event.code == C1_RIGHT2:
                self.objects.append(player1.build())  # todo what da Fu
        elif player == 2:
            if event.code == C2_BUTTON_DOWN:
                player2.move(Direction.DOWN)
            elif event.code == C2_BUTTON_UP:
                player2.move(Direction.UP)
            elif event.code == C2_BUTTON_LEFT:
                player2.move(Direction.LEFT)
            elif event.code == C2_BUTTON_RIGHT:
                player2.move(Direction.RIGHT)
            elif event.code == C2_LEFT1:
                player2.heal()
            elif event.code == C2_LEFT2:
                player2.hit(player1)
            elif event.code == C2_RIGHT1:
                projectile = player2.shoot(get_image('projectile.png'))
                self.projectiles.append(projectile)
            elif event.code == C2_RIGHT2:
                self.objects.append(player2.build())  # todo what da Fu

    def loop(self, to_remove):
        to_remove.clear()
        for i in range(len(self.projectiles)):
            current_projectile = self.projectiles[i]
            current_projectile.move()
            if not 0 < current_projectile.x < self.width or not 0 < current_projectile.y < self.height:
                to_remove.add(i)

            for player in (player1, player2):
                if player is not current_projectile.player and player.collides_with(current_projectile):
                    player.hp -= current_projectile.damage
                    to_remove.add(i)

        self.projectiles = list(
            filter(lambda proj: self.projectiles.index(proj) not in to_remove, self.projectiles)
        )
        self.clock.tick(60)

    def render(self):
        self.hp1 = self.font.render("HP:" + str(player1.hp), True, (0, 0, 0))
        self.hp2 = self.font.render("HP:" + str(player2.hp), True, (0, 0, 0))
        self.screen.fill((255, 255, 255))
        self.screen.blit(get_image('bg_image.png'), (0, 0))
        for current_object in self.objects:
            current_object.render(self.screen)
        for projectile in self.projectiles:
            projectile.render(self.screen)
        self.hp1 = self.font.render("HP:" + str(player1.hp), True, (0, 0, 0))
        self.hp2 = self.font.render("HP:" + str(player2.hp), True, (0, 0, 0))
        self.screen.blit(self.hp1, (50, 300))
        self.screen.blit(self.hp2, (500, 300))

        rect_player1 = pygame.Rect(player1.frame * 32, 32 * player1.current_facing.value, 32, 32)
        rect_player2 = pygame.Rect(player2.frame * 32, 32 * player2.current_facing.value, 32, 32)
        self.screen.blit(player1.image, (player1.x, player1.y), rect_player1)
        self.screen.blit(player2.image, (player2.x, player2.y), rect_player2)
        player1.frame += 1
        player2.frame += 1
        if player1.frame >= 9:
            player1.frame = 0
        if player2.frame >= 9:
            player2.frame = 0
        pygame.display.flip()

    @staticmethod
    def cleanup():
        pygame.quit()

    def execute(self):
        self.on_init()
        to_remove = set()
        self.screen.fill((255, 255, 255))
        self.render()
        while self._running:
            event1 = gamepad1.read_one()
            event2 = gamepad2.read_one()
            if event1 is not None and event1.type == ecodes.EV_KEY:
                self.on_event(event1, 1)
            if event2 is not None and event2.type == ecodes.EV_KEY:
                self.on_event(event2, 2)
            self.loop(to_remove)
            self.render()
        self.cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.execute()
