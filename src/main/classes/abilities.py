from .stone import Stone
from .direction import Direction
from config.game_config import SCREEN_WIDTH, SCREEN_HEIGHT
from classes.stone import Stone


MAX_STONES_WIDTH = SCREEN_WIDTH // Stone.SIZE
MAX_STONES_HEIGHT = SCREEN_HEIGHT // Stone.SIZE


class Ability:
    def __init__(self, name, ab_type, cooldown):
        self.name = name
        self.ab_type = ab_type
        self.cool = cooldown
        self.current_cooldown = 0
        self.invoke = None

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        self.invoke()


class Heal(Ability):
    def __init__(self, cooldown, amount, max_hp=100):
        super().__init__("Heal", "passive", cooldown)
        self.amount = amount
        self.max_hp = max_hp

    def __call__(self, *args, **kwargs):
        if args[0].hp + self.amount <= self.max_hp:
            args[0].hp += self.amount
        else:
            args[0].hp = self.max_hp
            

class Build(Ability):
    grid = [
        [0 for y in range(MAX_STONES_WIDTH)]
        for x in range(MAX_STONES_HEIGHT)
    ]

    def __init__(self, cooldown, hp):
        super().__init__("Build", "active", cooldown)
        self.image = "wall.png"  # set file path
        self.hp = hp

    def __call__(self, *args, **kwargs):
        facing = args[0].current_facing
        player = args[0]
        x = player.x
        y = player.y
        offset = 32
        stone = Stone(x, y, self.image, 100)
        if facing == Direction.UP:
            stone.y -= 32
            stone.x += offset
        if facing == Direction.DOWN:
            stone.y += 64
            stone.x += offset
        if facing == Direction.LEFT:
            stone.x -= 32
            stone.y += offset
        if facing == Direction.RIGHT:
            stone.x += 64
            stone.y += offset

        offset_x = stone.x % Stone.SIZE
        offset_y = stone.y % Stone.SIZE
        if offset_x < Stone.SIZE // 2:
            new_x = stone.x - offset_x
        else:
            new_x = stone.x + Stone.SIZE - offset_x
        if offset_y < Stone.SIZE // 2:
            new_y = stone.y - offset_y
        else:
            new_y = stone.y + Stone.SIZE - offset_y 
        #new_y = stone.y - (stone.y % Stone.SIZE)
        ind_x = new_x // 32
        ind_y = new_y // 32
        if 0 <= ind_x < MAX_STONES_WIDTH and 0 <= ind_y < MAX_STONES_HEIGHT:
            if self.grid[ind_y][ind_x] == 1:
                return None
            stone.x = new_x
            stone.y = new_y
            stone.grid_x = ind_x
            stone.grid_y = ind_y
            self.grid[ind_y][ind_x] = 1
            return stone

