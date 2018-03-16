
class Ability:
    def __init__(self, name, ab_type, cooldown, image=None):
        self.name = name
        self.ab_type = ab_type
        self.cool = cooldown
    def __str__(self):
        return self.name

    def hp_change(self,pl, amount):
        pl.hp = amount

    def dmg_change(self, proj, dmg):
        proj.dmg = dmg
