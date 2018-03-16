import pygame

from evdev import InputDevice, categorize, ecodes
from classes import player
from helpers.image_getter import get_image
from controller_config import *


#setting up gamepad
gamepad = InputDevice('/dev/input/event3')
gamepad2 = InputDevice('/dev/input/event4')

# setting up players
player1 = player.Player(50, 500, get_image('player.png'))  # TODO: add later
player2 = player.Player(450, 500, get_image('player.png'))  # TODO: add later
#main class
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 640, 400
        self.clock = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.SRCALPHA)
        self._running = True
        self.clock = pygame.time.Clock()


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.code == c1_down_btn:
            player1.move_down()
        if event.code == c1_up_btn:
            player1.move_up()
        if event.code == c1_left_btn:
            player1.move_left()
        if event.code == c1_right_btn:
            player1.move_right()
        # player 2 buttons :

        if event.code == c2_down_btn:
            player2.move_down()
        if event.code == c2_up_btn:
            player2.move_up()
        if event.code == c2_left_btn:
            player2.move_left()
        if event.code == c2_right_btn:
            player2.move_right()
    def loop(self):
        self.clock.tick(60)

    def render(self):
        self.screen.blit(get_image('player.png'), (player1.x,player1.y))
        self.screen.blit(get_image('player.png'), (player2.x, player2.y))

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event1, event2 in gamepad.read_loop(), gamepad2.read_loop():
                if event1.type == ecodes.EV_KEY:
                    if event1.value == 1:
                        self.on_event(event1)
                if event2.type == ecodes.EV_KEY:
                    if event2.value == 1:
                        self.on_event(event2)
            self.loop()
            self.render()
        self.cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.execute()
