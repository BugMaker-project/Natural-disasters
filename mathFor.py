import numpy as np
import scipy as sp
import time
def CrashArray():
    arraylist=[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,
               6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,11,11,12,
               13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13]
    arraylist=np.asarray(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    arraylist=np.random.permutation(arraylist)
    return arraylist
