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
def start()
while True:
    handleEvent()
    pygame.time.delay(10)
    pygame.display.update()
