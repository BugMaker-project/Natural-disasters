import numpy as np
import scipy as sp
import time
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
def SuccessProbability():
    #成功概率列表
    SuccessProbabilityArray=[0,0,0,0,0,0,1,1,1,1,1,1]
    #改为array阵列类型
    SuccessProbabilityArray=np.asarray(SuccessProbabilityArray)
    #4次随机打乱
    SuccessProbabilityArray=np.random.permutation(SuccessProbabilityArray)
    SuccessProbabilityArray=np.random.permutation(SuccessProbabilityArray)
    SuccessProbabilityArray=np.random.permutation(SuccessProbabilityArray)
    SuccessProbabilityArray=np.random.permutation(SuccessProbabilityArray)
    #获取随机取出的返回
    SuccessProbabilityReponse=np.random.choice(SuccessProbabilityArray)
    if SuccessProbabilityReponse==0:
        #当返回==0，返回值为“Success”
        return "Success"
    else:
        #当返回==1，返回值为“Failure”
        return "Failure"
    
