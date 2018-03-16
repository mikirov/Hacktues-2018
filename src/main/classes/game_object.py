class GameObject:
    def __init__(self, start_x, start_y, speed=1):
        self.x = start_x
        self.y = start_y
        self.speed = speed

    def move_up(self, step):
        self.y -= step * speed

    def move_down(self, step):
        self.y += step * speed

    def move_right(self, step):
        self.x += step * speed

    def move_left(self, step):
        self.x -= step * speed

