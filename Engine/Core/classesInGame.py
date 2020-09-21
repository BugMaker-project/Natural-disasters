import pygame
class Background(object):
    def __init__(self,image):
        self.x=0
        self.y=0
        self.image=image
    def load(self):
        self.image=pygame.image.load(self.image)