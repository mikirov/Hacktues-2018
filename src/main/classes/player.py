from .game_object import GameObject


class Player(GameObject):
    def __init__(self, start_x, start_y, image_width, image_height,
            image_filepath, speed=1, hp=100):
        super().__init__(start_x, start_y, image_width, image_height,
            image_filepath, speed)
        self.hp = hp

    def shoot(self):
        pass 

    def image_details(self):
        return "image: '{}, size: ({}, {})'".format(
            self.image_filepath, self.image_width, self.image_height
        )

