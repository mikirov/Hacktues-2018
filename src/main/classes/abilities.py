from .game_object import GameObject
from .direction import Direction

class Ability:
    def __init__(self, name, ab_type, cooldown):
        self.name = name
        self.ab_type = ab_type
        self.cool = cooldown
        self.current_cooldown = 0
        self.func = None
    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        self.func()

    def hp_change(self,pl, amount):
        pl.hp = amount

    def dmg_change(self, proj, dmg):
        proj.dmg = dmg

class Heal(Ability):
    def __init__(self, cooldown, amount):
        super().__init__("Heal","passive", cooldown)
        self.amount = amount

    def __call__(self, *args, **kwargs):
        args[0].hp += self.amount

class Build(Ability):
    def __init__(self, cooldown):
        super().__init__("Build", "active",cooldown)
        self.image_filepath = "stone.png" # set file path

    def __call__(self, *args, **kwargs):

        facing = args[0].current_facing
        player = args[0]
        screen = args[1]
        x = args[0].x
        y = args[0].y
        stone = GameObject(x, y, self.image_filepath)
        if facing == Direction.UP: 
            stone.y -= 5
        if facing == Direction.DOWN:
            stone.y += 5
        if facing == Direction.LEFT: 
            stone.x -= 5
        if facing == Direction.RIGHT: 
            stone.x += 5

        return stone
