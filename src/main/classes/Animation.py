import pygame
class Animation:
    def __init__(self, owner, width, height, max_frames, frame = 0, speed = 0.5,):
        self.owner = owner
        self.starting_frame = frame
        self.frame = frame
        self.max_frames = max_frames
        self.speed = speed
        self.width = width
        self.height = height



    def play(self, screen, loop=True):
        current_frame = pygame.Rect(int(self.frame) * self.width, self.height * self.owner.current_facing.value,
                                   self.width, self.height)
        screen.blit(self.owner.image, (self.owner.x, self.owner.y), current_frame)
        self.frame += self.speed
        if loop and self.frame >= self.max_frames:
            self.frame = self.starting_frame

    def stop(self, screen):
        current_frame = pygame.Rect(int(self.starting_frame) * self.width, self.height * self.owner.current_facing.value,
                                    self.width, self.height)
        screen.blit(self.owner.image, (self.owner.x, self.owner.y), current_frame)