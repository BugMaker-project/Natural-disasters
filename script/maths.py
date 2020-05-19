import numpy as np
import scipy as sp
import time,random
def CrashArray():
    #创建基础列表
    arraylist=[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,
               6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,11,11,12,
               13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13]
    #改为array阵列类型
    arraylist=np.asarray(arraylist)
    #8次随机打乱后返回
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    return arraylist
def SuccessProbability(mode):
    #成功概率列表
    if mode=="Normally":
        SuccessProbabilityArray=[0,0,0,0,0,0,1,1,1,1,1,1]
    elif mode=="Difficult":
        SuccessProbabilityArray=[0,0,0,0,1,1,1,1,1,1,1,1]
    elif mode=="Easy":
        SuccessProbabilityArray=[0,0,0,0,0,0,0,0,1,1,1,1]
    elif mode=="Most Difficult":
        SuccessProbabilityArray=[0,0,0,1,1,1,1,1,1,1,1,1]
    elif mode=="Most Easy":
        SuccessProbabilityArray=[0,0,0,0,0,0,0,0,0,1,1,1]
    #改为array阵列类型
    SuccessProbabilityArray=np.asarray(SuccessProbabilityArray)
    #10次随机打乱
    for i in range(10):
        SuccessProbabilityArray=np.random.permutation(SuccessProbabilityArray)
    #获取随机取出的返回
    SuccessProbabilityReponse=np.random.choice(SuccessProbabilityArray)
    if SuccessProbabilityReponse==0:
        #当返回==0，返回值为“Success”
        return "Success"
    else:
        #当返回==1，返回值为“Failure”
        return "Failure"
#缺氧检测函数
def Anoxia(Environmental):
    #深海条件下的氧气(1==氧气，2==毒气，0==无效气体，3==核污染气体)
    if Environmental=="DeepSea":
        OxygenArray=[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
    #浅水条件
    elif Environmental=="ShallowWater":
        OxygenArray=[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
    #化学污染区
    elif Environmental=="ChemicalPollutionArea":
        OxygenArray=[1,1,1,1,1,1,1,1,1,1,0,0,2,2,2,2,2,2]
    #核污染区
    elif Environmental=="NuclearPollutionArea":
        OxygenArray=[1,1,1,1,1,1,1,1,0,0,0,2,2,2,3,3,3,3]
    #正常环境
    elif Environmental=="Normal":
        OxygenArray=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #构建numpy数组
    OxygenArray=np.asarray(OxygenArray)
    #10次打乱数组
    for e in range(10):
        np.random.shuffle(OxygenArray)
    #随机取数
    ifAnoxia=np.random.choice(OxygenArray)
    #判断并返回值
    if ifAnoxia==1:
        return "Normally"
    elif ifAnoxia==0:
        return "Anoxia"
    elif ifAnoxia==2:
        return "Chemical"
    elif ifAnoxia==3:
        return "Nuclear"
#反对科学组织的前置函数,请不要单独调用！
def ASPRandoms(nums):
    #随机取的数字确定执行方法
    choice=random.randint(0,4)
    if choice>=1:
        #方案A
        nums+=2
    else:
        #B
        nums-=2
    return nums
#反对科学组织的生成概率
def AgainstScientificProbability():
    #生成概率列表哦
    Alpha=[]
    listofProbability=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    #Map批量执行
    listofProbability=map(ASPRandoms,listofProbability)
    #循环迭代并添加
    for i in listofProbability:
        if i!=2:
            Alpha.append(True)
        else:
            Alpha.append(False)
    #打乱循环迭代后的列表
    for j in range(5):
        random.shuffle(Alpha)
    #返回
    return random.choice(Alpha)

