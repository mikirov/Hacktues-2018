from .stone import Stone
from .direction import Direction


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
    def __init__(self, cooldown, hp):
        super().__init__("Build", "active", cooldown)
        self.image = "wall.png"  # set file path
        self.hp = hp

    def __call__(self, *args, **kwargs):
        facing = args[0].current_facing
        player = args[0]
        x = player.x
        y = player.y
        offset = 16
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
        return stone

