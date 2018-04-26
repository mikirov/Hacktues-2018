import pygame
class Animation:
    def __init__(self, owner, max_frames, rows, name=None, frame = 0, image=None, speed = 0.5,loop=True):
        self.owner = owner
        self.name = name
        self.image = image or owner.image
        self.starting_frame = frame
        self.frame = frame
        self.max_frames = max_frames
        self.speed = speed
        self.width = self.image.get_width() / max_frames
        self.height = self.image.get_height() / rows
        self.playing = False
        self.loop = loop





    def play(self, screen):
        self.playing = True
        current_frame = pygame.Rect(int(self.frame) * self.width, self.height * self.owner.current_facing.value,
                                   self.width, self.height)
        screen.blit(self.image, (self.owner.x, self.owner.y), current_frame)
        self.frame += self.speed
        if self.frame >= self.max_frames:
            if self.loop is False:
                self.stop(screen)
                return
            self.frame = self.starting_frame



    def stop(self, screen):
        self.playing = False
        current_frame = pygame.Rect(int(self.starting_frame) * self.width, self.height * self.owner.current_facing.value,
                                    self.width, self.height)
        screen.blit(self.owner.image, (self.owner.x, self.owner.y), current_frame)