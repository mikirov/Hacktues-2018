class Ability:
    def __init__(self, name, ab_type, cooldown, image=None):
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

class Build(Ability): # set file path
    def __init__(self, cooldown):
        super().__init__("Build", "active",cooldown)

    def __call__(self, *args, **kwargs):
        facing = args[0].current_facing
        if facing == 0:
            pass
        if facing == 1:
            pass
        if facing == 2:
            pass
        if facing == 3:
            pass