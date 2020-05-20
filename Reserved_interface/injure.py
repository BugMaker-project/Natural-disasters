import random as rd
from decimal import *
#创建伤害控制类
class Injure(object):
    def __init__(self,blood:Decimal,intelligence:Decimal,spirit:Decimal,\
                 PhysicalFitness:Decimal,ArmorBlood:Decimal):
        self.blood=blood #血量
        self.intelligence=intelligence #智力
        self.spirit=spirit #精神
        self.PhysicalFitness=PhysicalFitness #体力
        self.ArmorBlood=ArmorBlood #装甲血量
        self.DeductionOfBloodVolume=None #单次扣血值
        self.DeductionOfBloodTime=None #总扣血时长（S）
        self.DeductionOfIntelligenceVolume=None #智商缩减值
        self.DeductionOfSpiritVolume=None #精神缩减值
        self.DeductionOfPhysicalFitnessVolume=None #体力扣减值
        self.DirectDamage=None #直接造成的伤害（未扣除装甲防御值）
    def ColdWeaponDamage(self):#定义冷兵器伤害
        self.DirectDamage=rd.randint(5,10)#随机获得一个造成的伤害
        if self.ArmorBlood>=80:#当护甲血量大于等于80
            self.DeductionOfBloodVolume=self.DirectDamage-3#总扣除血量=直接伤害-3
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(2,5)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
        elif self.ArmorBlood>=50:#当护甲血量大于等于50
            self.DeductionOfBloodVolume=self.DirectDamage-1#总扣除血量=直接伤害-1
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(5,9)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
        elif self.ArmorBlood<50 and self.ArmorBlood>0:#当护甲血量小于50且不为0或负数
            self.DeductionOfBloodVolume=self.DirectDamage#总扣除血量=直接伤害
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(15,19)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
        else:#当护甲血量为0或负数
            self.DeductionOfBloodVolume=self.DirectDamage#总扣除血量=直接伤害
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.DeductionOfBloodVolume+=rd.randint(5,15)#在总扣除血量中增加破甲损伤
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None

    def HotWeaponDamage(self):#定义热兵器伤害
        self.DirectDamage=rd.randint(15,20)#随机获得一个造成的伤害
        if self.ArmorBlood>=80:#当护甲血量大于等于80
            self.DeductionOfBloodVolume=self.DirectDamage-7#总扣除血量=直接伤害-7
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            ifBreakdown=bool(rd.randint(0,1))#判断是否击穿
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            if ifBreakdown:#如果击穿
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.DeductionOfBloodTime=rd.randint(1,5)#设置燃烧时间
            self.DeductionOfBloodVolume+=self.DeductionOfBloodTime*rd.randint(2,5)#设置燃烧血量
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(4,20)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
        elif self.ArmorBlood>=50:#当护甲血量大于等于50
            self.DeductionOfBloodVolume=self.DirectDamage-5#总扣除血量=直接伤害-5
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            ifBreakdown=bool(rd.randint(0,1))#判断是否击穿
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            if ifBreakdown:#如果击穿
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.DeductionOfBloodTime=rd.randint(1,5)#设置燃烧时间
            self.DeductionOfBloodVolume+=self.DeductionOfBloodTime*rd.randint(2,5)#设置燃烧血量
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(10,30)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
        elif self.ArmorBlood<50 and self.ArmorBlood>0:#当护甲血量小于50且不为0或负数
            self.DeductionOfBloodVolume=self.DirectDamage-3#总扣除血量=直接伤害-3
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            ifBreakdown=bool(rd.randint(0,1))#判断是否击穿
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            if ifBreakdown:#如果击穿
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.DeductionOfBloodTime=rd.randint(1,5)#设置燃烧时间
            self.DeductionOfBloodVolume+=self.DeductionOfBloodTime*rd.randint(2,5)#设置燃烧血量
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(4,20)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
        else:#当护甲血量为0或负数
            self.DeductionOfBloodVolume=self.DirectDamage#总扣除血量=直接伤害
            ifInfected=bool(rd.randint(0,1))#判断是否感染
            ifBreakdown=bool(rd.randint(0,1))#判断是否击穿
            if ifInfected:#如果感染
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            if ifBreakdown:#如果击穿
                self.DeductionOfBloodVolume+=3#需要扣除的血量+3
            self.DeductionOfBloodTime=rd.randint(1,5)#设置燃烧时间
            self.DeductionOfBloodVolume+=self.DeductionOfBloodTime*rd.randint(2,5)#设置燃烧血量
            self.blood-=self.DeductionOfBloodVolume#扣除对应血量
            self.ArmorBlood-=rd.randint(4,20)#护甲扣除随机数值
            self.DeductionOfBloodVolume=None#回归初始化
            self.DirectDamage=None
    def Fire(self):#定义烧伤
        self.DirectDamage=rd.randint(10,15)#取单次伤害
        self.DeductionOfBloodTime=rd.randint(5,10)#取随机时间
        self.DeductionOfBloodVolume=self.DeductionOfBloodTime*self.DirectDamage#计算扣除总血量
        self.blood-=self.DeductionOfBloodVolume#扣除血量
        self.DeductionOfBloodVolume=None#回归初始化
        self.DirectDamage=None
    def Chemical(self):#定义化学伤
        self.DirectDamage=rd.randint(10,15)#取单次伤害
        self.DeductionOfBloodTime=rd.randint(5,10)#取随机时间
        self.DeductionOfBloodVolume=self.DeductionOfBloodTime*self.DirectDamage+rd.randint(0,15)#计算扣除总血量
        self.blood-=self.DeductionOfBloodVolume#扣除血量
        self.DeductionOfBloodVolume=None  # 回归初始化
        self.DirectDamage=None
    def Freeze(self,time:Decimal):#冻结伤害
        self.DirectDamage=rd.randint(10,15)
        self.DeductionOfBloodTime=time
        self.DeductionOfBloodVolume=self.DeductionOfBloodTime*self.DirectDamage
        self.blood-=self.DeductionOfBloodVolume
        self.DeductionOfBloodVolume,self.DirectDamage=None,None
    def Insanity(self,degree:int):#精神错乱
        self.DeductionOfIntelligenceVolume=rd.randint(degree/3,degree)
        self.intelligence-=self.DeductionOfIntelligenceVolume
        self.spirit-=self.DeductionOfIntelligenceVolume/3
        self.DeductionOfIntelligenceVolume=None
    def 