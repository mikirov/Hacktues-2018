class GameObject:
    def __init__(self, start_x, start_y, image_filepath, speed=1):
        self.x = start_x
        self.y = start_y
        self.image_filepath = image_filepath
        self.speed = speed

    def move_up(self, step):
        self.y -= step * self.speed

    def move_down(self, step):
        self.y += step * self.speed

    def move_right(self, step):
        self.x += step * self.speed

    def move_left(self, step):
        self.x -= step * self.speed

