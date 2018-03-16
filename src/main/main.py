import pygame
from time import time

from evdev import InputDevice, categorize, ecodes
from classes import player
from classes import projectile
from helpers.image_getter import get_image
from controller_config import *
from classes.direction import Direction


# set up gamepad
gamepad1 = InputDevice('/dev/input/event2')
# gamepad2 = InputDevice('/dev/input/event4')

# set up players
player1 = player.Player(50, 50, 'player.png')  
player2 = player.Player(150, 50, 'player.png')
objects = []
# main class
class App:
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 640, 400
        self.clock = None
        self.projectiles = []

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.SRCALPHA)
        self._running = True
        self.clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.code == c1_down_btn:
            player1.move(Direction.DOWN)
            player1.image_filepath = 'backpl.png'
        elif event.code == c1_up_btn:
            player1.move(Direction.UP)
            player1.image_filepath = 'frontpl.png'
        elif event.code == c1_left_btn:
            player1.move(Direction.LEFT)
            player1.image_filepath = 'leftpl.png'
        elif event.code == c1_right_btn:
            player1.move(Direction.RIGHT)
            player1.image_filepath = 'rightpl.png'
        elif event.code == c1_l1:
            player1.heal() 
        elif event.code == c1_l2:
            player1.hit()
        elif event.code == c1_r1:
            projectile = player1.shoot()
            self.projectiles.append(projectile)
        elif event.code == c1_r2:
            objects.append(player1.build(player1))

        # player 2 buttons :

        elif event.code == c2_down_btn:
            player2.move(Direction.DOWN)
        elif event.code == c2_up_btn:
            player2.move(Direction.UP)
        elif event.code == c2_left_btn:
            player2.move(Direction.LEFT)
        elif event.code == c2_right_btn:
            player2.move(Direction.RIGHT)
        
        elif event.code == c2_l1:
            pass        
        elif event.code == c2_l2:
            pass
        elif event.code == c2_r1:
            pass
        elif event.code == c2_r2:
            pass

    def loop(self):
        self.clock.tick(60)

    def render(self):
        self.screen.blit(get_image(player1.image_filepath), (player1.x, player1.y))
        self.screen.blit(get_image(player2.image_filepath), (player2.x, player2.y))

        for prj in self.projectiles:
            self.screen.blit(get_image(prj.image_filepath), (prj.x, prj.y))
        for obj in objects:
            self.screen.blit(get_image(obj.image_filepath), (obj.x, obj.y))

        pygame.display.flip()

    def cleanup(self):
        pygame.quit()

    def execute(self):
        if self.on_init() == False:
            self._running = False

        current_time = time()
        self.screen.fill((255, 255, 255))
        self.render()
        for event1 in gamepad1.read_loop():
            print("Projectiles:", len(self.projectiles))

            if not self._running:
                break
            previous_time = current_time
            current_time = time()
            time_delta = current_time - previous_time 

            to_remove = set()
            for i in range(0, len(self.projectiles)):
                prj = self.projectiles[i]
                prj.move(time_delta)
                if not 0 <= prj.x <= self.width or not 0 <= prj.y <= self.height:
                    to_remove.add(i)

            print(len(to_remove))
            self.projectiles = list(filter(lambda prj: not prj in to_remove, self.projectiles))

            self.projectiles = list(filter(lambda prj: self.projectiles.index(prj) not in to_remove, self.projectiles))

            if event1.type == ecodes.EV_KEY:
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


if __name__ == "__main__" :
    theApp = App()
    theApp.execute()

