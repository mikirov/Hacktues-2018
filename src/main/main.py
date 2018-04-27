import pygame
from time import *

import evdev
from classes import player
from classes import projectile
from classes.abilities import *
from helpers.image_getter import get_image
from controller_config import *
#from keyboard_config import *
from classes.direction import Direction
from classes.stone import Stone
from select import select
from classes.Animation import Animation
import random
# set up gamepad
#TODO Fix heal animation



def find_device(name):
    ls = [evdev.InputDevice(dev) for dev in evdev.list_devices()]
    filtered = list(filter(lambda x: name in x.name, ls))
    return filtered[0] if len(filtered) > 0 else None

#gamepad1 = InputDevice('/dev/input/event2')
#gamepad2 = InputDevice('/dev/input/event1')
#gamepad1 = list(filter(lambda x: "Micro" in x.name,ls))[0]
#gamepad2 = list(filter(lambda x: "Dragon" in x.name, ls))[0]
gamepad1 = find_device("Micro")
gamepad2 = find_device("Dragon")

# set up players
player1 = player.Player(50, 150, get_image('mage_one.png'))
player2 = player.Player(300, 150, get_image('mage_two.png'))

#rect_player1 = pygame.Rect(player1.frame * 64, 64 * player1.current_facing.value, 64, 64)
#rect_player2 = pygame.Rect(player2.frame * 64, 64 * player2.current_facing.value, 64, 64)
player1.update_hitbox()
player2.update_hitbox()
player1.add_animation(9,4) # base_animation
player2.add_animation(9,4)
player1.add_animation(6,1, image=get_image('heal_anim2.png'), name="heal", offset_x=-3,offset_y=-35, loop=False)
player2.add_animation(6,1, image=get_image('heal_anim2.png'), name="heal",offset_x=-3,offset_y=-35, loop=False)
FONT_SIZE = 60


COOLDOWN = 0.5 # in seconds


# main class
class App:
    def __init__(self, debug=False):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 620, 350
        self.clock = None
        self.projectiles = []
        self.draw_hitboxes = debug
        self.objects = [player1, player2]

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self._running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

    def on_event(self, event, player, keyboard):
        print("Processing input\n")
        if event.code == EXIT_BUTTON:
            self._running = False
        if player == 1:
            if event.code == C1_BUTTON_DOWN:
                player1.move(Direction.DOWN, self.objects)
            elif event.code == C1_BUTTON_UP:
                player1.move(Direction.UP, self.objects)
            elif event.code == C1_BUTTON_LEFT:
                player1.move(Direction.LEFT, self.objects)
            elif event.code == C1_BUTTON_RIGHT:
                player1.move(Direction.RIGHT, self.objects)
            elif event.code == C1_LEFT1:
                player1.heal()
            elif event.code == C1_LEFT2:
                player1.hit(player2)  # incomplete
            elif event.code == C1_RIGHT1:
                current_time = time()
                if current_time -  player1.last_projectile_fired_at >= COOLDOWN:
                    projectile = player1.shoot(get_image('fireball.png'))
                    self.projectiles.append(projectile)
                    player1.last_projectile_fired_at = current_time
            elif event.code == C1_RIGHT2:
                stone = player1.build()
                if stone is not None:
                    stone.image = get_image(stone.image)
                    stone.make_hitbox()
                    if not player1.collides_with(stone):
                        self.objects.append(stone)  # todo what da Fu
        if keyboard is not None:
            player = 2
        if player == 2:
            if event.code == C2_BUTTON_DOWN:
                player2.move(Direction.DOWN, self.objects)
            elif event.code == C2_BUTTON_UP:
                player2.move(Direction.UP, self.objects)
            elif event.code == C2_BUTTON_LEFT:
                player2.move(Direction.LEFT, self.objects)
            elif event.code == C2_BUTTON_RIGHT:
                player2.move(Direction.RIGHT, self.objects)
            elif event.code == C2_LEFT1:
                player2.heal()
            elif event.code == C2_LEFT2:
                player2.hit(player1)
            elif event.code == C2_RIGHT1:
                current_time = time()
                if current_time - player2.last_projectile_fired_at >= COOLDOWN:
                    projectile = player2.shoot(get_image('iceball.png'))
                    self.projectiles.append(projectile)
                    player2.last_projectile_fired_at = current_time
            elif event.code == C2_RIGHT2:
                stone = player2.build()
                if stone is not None:
                    stone.image = get_image(stone.image)
                    stone.make_hitbox()
                    if not player2.collides_with(stone):
                        self.objects.append(stone)  # todo what da Fu

    def loop(self, to_remove):
        to_remove.clear()
        to_remove_objs = set()
        for pl in (player1, player2): # update players version
            pl.objects = self.objects

        for current_proj in self.projectiles:
            current_proj.move()
            all = current_proj.get_colliders(self.objects)
            if len(all) == 0: continue
            print("Removed projectile.")
            to_remove.add(current_proj)
            for obj in all:
                if isinstance(obj, Stone) or isinstance(obj, player1.__class__):
                    obj.hp -= current_proj.damage
                    if obj.hp <= 0:
                        to_remove_objs.add(obj)

        self.projectiles = list(
            filter(lambda proj: proj not in to_remove, self.projectiles)
        )

        self.objects = list(
            filter(lambda obj: obj not in to_remove_objs, self.objects)
        )

        if player1.hp <= 0 or player2.hp <=0:
            if player1.hp <= 0:
                pl = player2
            else:
                pl = player1
           # self.winner = self.font.render("Player:" + str(pl), True, (0, 0, 0))
            #self.screen.blit(self.winner, (400, 400))
            #sleep(2)
            self.reset()
        self.clock.tick(20)

    def render(self):
        self.hp1 = self.font.render("HP:" + str(player1.hp), True, (0, 0, 0))
        self.hp2 = self.font.render("HP:" + str(player2.hp), True, (0, 0, 0))
        self.screen.fill((255, 255, 255))
        self.screen.blit(get_image('test.png'), (0, 0))
        for current_object in self.objects:
            if current_object == None or current_object == player1 or current_object == player2:
                continue
            #current_object.render(self.screen)
            current_object.render(self.screen, self.draw_hitboxes)
        for projectile in self.projectiles:
            projectile.render(self.screen, self.draw_hitboxes)
        self.hp1 = self.font.render("HP:" + str(player1.hp), True, (0, 0, 0))
        self.hp2 = self.font.render("HP:" + str(player2.hp), True, (0, 0, 0))
        self.screen.blit(self.hp1, (50, 300))
        self.screen.blit(self.hp2, (400, 300))
        if self.draw_hitboxes:
            player1.render_hitbox(self.screen)
            player2.render_hitbox(self.screen)

        player1.base_animation.play(self.screen, player1.current_facing.value)
        player2.base_animation.play(self.screen, player2.current_facing.value)

        for pl in (player1, player2):
            for animation in pl.animations[1:]:
                if animation.playing:
                    animation.play(self.screen, 0) # play default first row


        pygame.display.flip()

    @staticmethod
    def cleanup():
        pygame.quit()

    def execute(self):
        self.on_init()
        to_remove = set()
        self.screen.fill((255, 255, 255))
        self.render()
        devices = [gamepad1, gamepad2, keyboard]
        devices = list(filter(lambda dev: dev is not None,devices))

        devs = {dev.fd: dev for dev in devices}

        while self._running:

            r,w,x = select(devs, [], [], 1/60)

            for fd in r:

                for event in devs[fd].read():

                    if event.type == evdev.ecodes.EV_KEY:

                        dev = devs[fd]
                        if dev is devices[0]:
                            p = 1
                        else:
                            p = 2
                        print(event.code)
                        self.on_event(event, p, keyboard)
            self.loop(to_remove)
            self.render()
        self.cleanup()

    def reset(self):
        self.projectiles = []
        self.objects = [player1, player2]
        player1.hp, player2.hp = 100, 100
        player1.x, player1.y = random.randint(10,250), random.randint(10, 250)
        player2.x, player2.y = random.randint(300,550), random.randint(10, 250)
        player1.update_hitbox()
        player2.update_hitbox()


if __name__ == "__main__":
    theApp = App()
    theApp.execute() # give True to enable hitbox drawing
