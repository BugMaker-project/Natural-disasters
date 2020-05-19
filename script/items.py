import pygame,math,random
from script.sprite import Sprite

land_sprite = pygame.image.load("../../image/land_sprite.png")



#定义单元格类
class Unit():
    def __init__(self,column,line,name,type,canvas,img="null"):
        #屏幕上的单元格坐标
        self.x = 0
        self.y = 0
        #地图中的坐标
        self.column = column
        self.line = line
        #名字
        self.name = name
        #种类
        self.type = type
        #贴图
        self.img = img
        #要绘制到的屏幕
        self.canvas = canvas
        self.index = 0
        self.index_width = 1
        self.index_height = 1
        #邻近可能会存在的方块
        self.neightbor_blocks = []
    def spawn(self):
        #通过单元格坐标获取实际坐标
        x = self.x * GameVar.index_width
        y = self.y * GameVar.index_height
        Sprite.draw(self.index,x,y,self.index_width,self.index_height)

#错误方块类
class Error(Unit):
    def __init__(self,column,line,canvas):
        Unit.__init__(self,column,line,"Error","error",canvas)
        self.index = 0
        self.index_height = 1
        self.index_width = 1

#草地类
class Grass_land(Unit):
    def __init__(self,column,line,canvas):
        Unit.__init__(column,line,"GrassLand","land",canvas)
        self.index = 1
        self.index_width = 1
        self.index_height = 1
        self.neightbor_blocks = [0]
    def get_neibor_block(self,dire):
        block_index = random.randint(0,len(self.neightbor_blocks)-1)
        block = self.neightbor_blocks[block_index]
        block_return = []
        if dire == "up":
            block.line = self.line + 1
            block.column = self.column
            block.canvas = self.canvas
            block_return.append(block)
            return block_return
        elif dire == "right":
            block.line = self.line
            block.column = self.column + 1
            block.canvas = self.canvas
            return block_return
        elif dire == "down":
            block.line = self.line - 1
            block.column = self.column
            block.canvas = self.canvas
            return block_return
        elif dire == "left":
            block.line = self.line
            block.column = self.column - 1
            block.canvas = self.canvas
            return block_return
        elif dire == "all":
            dires = ["up","right","down","left"]
            for dires in dire:
                block_return.append(self.get_neibor_block(dire))
            return block_return



block_dictionary = [Grass_land(0,0,"null_canvas",1,1,1)]