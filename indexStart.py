import pygame
from pygame.locals import *
import sys,json,time
#创建一个canvas并填为白色
pygame.init()
canvas=pygame.display.set_mode([1280,720])
canvas.fill([255,255,255])
def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
def isActionTime(lastTime,interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime - lastTime >= interval
class GameVar():
    gameInfo=None
    GameState="Start"
def jsonGot():
    with open(".\Data\Info.json") as o:
        result=o.read()
        result=json.loads(result)
        GameVar.gameInfo=result
jsonGot()
while True:
    handleEvent()
    pygame.time.delay(10)
    pygame.display.update()