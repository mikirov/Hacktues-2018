class Abilities:
    def __init__(self, name, ab_type, image=None):
        self.name = name
        self.ab_type = ab_type
    def __str__(self):
        return self.name