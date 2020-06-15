import time
timeStart=None
def init():
    global timeStart
    if timeStart==None:
        local=time.localtime()
        timeStart=local.tm_hour*3600+local.tm_min*3600+local.tm_sec
class Tick(object):
    def __init__(self):
        self.local=time.localtime()
        self.date=[self.local.tm_year,self.local.tm_mon,self.local.tm_mday]
        self.time=self.local.tm_hour*3600+self.local.tm_min*3600+self.local.tm_sec
        self.Gametick=(self.time-timeStart)/0.25
    def update(self):
        self.local=time.localtime()
        self.date=[self.local.tm_year,self.local.tm_mon,self.local.tm_mday]
        self.time=self.local.tm_hour*3600+self.local.tm_min*3600+self.local.tm_sec
        self.Gametick=(self.time-timeStart)/0.25
class Day(object):
    def __init__(self):
        self.length=4800.0
        self.day=1
        self.passTime=0
        self.stutes="Morning"
    def update(self):
        if self.passTime>=self.length:
            self.day+=1
            self.passTime=0
        
