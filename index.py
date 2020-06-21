import pygame
from pygame.locals import *
import sys,json,time
from script import Error,colorfulText,Control,Crash,injure
from script import items,Keys,Logs,maths,sprite,timers,var,world_create
back1=pygame.image.load(var.PATHS.backStart)
#创建一个canvas并填为白色
pygame.init()
canvas=pygame.display.set_mode([640,360])
canvas.fill([255,255,255])
#创建handleEvent函数
def handleEvent():
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_ESCAPE or event.type==QUIT:
            pygame.quit()
            sys.exit()

#isActionTime方法控制延时
def isActionTime(lastTime,interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime - lastTime >= interval





class BackGround():
    def __init__(self):
        self.x = 0
        self.y = 0
        
        
class GameVar():
    #单元格长宽
    index_width = 16
    index_height = 16
    gameInfo=None
    #State:[HOME,START,RUNNING,QUIT]
    GameState="HOME"
    back=BackGround()
    
    
def jsonGot():
    with open(r".\Data\Info.json") as o:
        result=o.read()
        result=json.loads(result)
        GameVar.gameInfo=result
def GameInit():
    jsonGot()

def control():
    if GameVar.GameState == "HOME":
        canvas.blit(back1,(GameVar.back.x,GameVar.back.y))
        pass
def main():
    control()
GameInit()
while True:
    main()
    handleEvent()
    pygame.time.delay(10)
    pygame.display.update()
