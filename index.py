import pygame
from pygame.locals import *
from Engine.Core import *
from Engine.Until import *
pygame.init()
canvas=pygame.display.set_mode([1280,720])
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
def start():
    bg=classesInGame.Background(imageFont_load.ImageSetting.background,canvas)
    bg.draw()
    title=classesInGame.Surface(imageFont_load.ImageSetting.title,498,65,500,500,canvas)
while True:
    start()
    handleEvent()
    pygame.time.delay(10)
    pygame.display.update()
