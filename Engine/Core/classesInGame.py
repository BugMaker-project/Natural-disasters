import pygame


class Background(object):
    def __init__(self, image, canvas):
        self.x = 0
        self.y = 0
        self.image = image
        self.canvas = canvas
        self.isLoadOver = False

    def load(self):
        self.image = pygame.image.load(self.image)
        self.isLoadOver = True

    def draw(self):
        if not self.isLoadOver:
            self.load()
        self.canvas.blit(self.image, (self.x, self.y))

class Surface(object):
    def __init__(self,image, x, y,height,width,canvas):
        self.x = x
        self.y = y
        self.image = image
        self.canvas = canvas
        self.height = height
        self.width = width
        self.load()
        self.draw()
    def load(self):
        self.imageObj=pygame.image.load(self.image)
        self.imageObj=pygame.transform.scale(self.imageObj, (self.width,self.height))
    def draw(self):
        self.canvas.blit(self.imageObj,(self.x, self.y))