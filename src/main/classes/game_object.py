class GameObject:
    def __init__(self, start_x, start_y, image_width, image_height,
            image_filepath, speed=1):
        self.x = start_x
        self.y = start_y
        self.image_width = image_width
        self.image_height = image_height
        self.image_filepath = image_filepath
        self.speed = speed

    def move_up(self, step=1):
        self.y -= step * self.speed

    def move_down(self, step=1):
        self.y += step * self.speed

    def move_right(self, step=1):
        self.x += step * self.speed

    def move_left(self, step=1):
        self.x -= step * self.speed

    def __str__(self):
        return '{} at (x: {}, y: {})'.format(
            self.__class__.__name__, self.x, self.y
        )

