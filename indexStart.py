import pygame
from pygame.locals import *
import sys
#创建一个canvas并填为白色
pygame.init()
canvas=pygame.display.set_mode([1280,720])
canvas.fill([255,255,255])
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
while True:
    handleEvent()
    pygame.time.delay(10)
    pygame.display.update()
