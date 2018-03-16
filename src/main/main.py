import pygame
from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event3')

from controller_config import *


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def loop(self):
        pass

    def render(self):
        pass

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        self.on_event(event.code)

            self.loop()
            self.render()
        self.cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.execute()
