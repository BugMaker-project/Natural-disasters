
class Sprite():
    def __init__(self,canvas,source,width,height):
        self.canvas = canvas
        self.source = source
        self.width = width
        self.height = height
        self.animation_index = 0
        self.animation_running = False
    def draw(self,index,x,y,index_width,index_height,source_width=500,source_height=500):
        #注：index_width和index_height表示的是Tile长宽的格数，也就是说Tile的长宽除以16
        source_width_index = source_width / self.width #资源图有多少格
        source_height_index = source_height / self.height #资源图有多少格
        index_column = index % source_width_index #实际的列
        index_line = (index - index_column) / source_height_index #实际的行
        img_x = index_column * self.width #资源图中Tile的x
        img_y = index_line * self.height #资源图中Tile的y
        width = index_width * self.width #资源图中Tile的width
        height = index_height * self.height #资源图中Tile的height
        self.canvas.blit(self.source,(x,y),(img_x,img_y,width,height)) #绘制
    def animation(self,x,y,width,height,start_index,over_index,state):
        if state == "over":
            self.animation_running = False
            return

        if not self.animation_running:
            self.animation_index = start_index
            self.animation_running = True
        self.draw(self.animation_index,x,y)
        self.animation_index += 1
        if self.animation_index > over_index:
            self.animation_index = start_index
