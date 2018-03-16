class Abilities:
    def __init__(self, name, type, image=None):
        self.name = name
        self.type = type
    def __str__(self):
        return self.name