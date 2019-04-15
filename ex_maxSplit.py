import itertools
import numpy as np
class maxSplit(object):
    def __init__(self,num,splitList=[]):
        self.num=num
        # self.splitList=[]
    def multipleMax(self):
        devide=[10**i for i in range(1,len(str(self.num)))]
        for i in devide:
            self.splitList.append((self.num//i,self.num%i))
        mulRes=[i[0]*i[1] for i in self.splitList]
        m=mulRes.index(max(mulRes))
        return self.splitList[m],mulRes[m]

class Mixmaxsplit(object):
    def __init__(self,num0):
        self.num0=num0
    def numAll(self):
        numList=[int(''.join(i)) for i in list(itertools.permutations(str(self.num0)))]
        return numList #here, no need to check if the num is start with 0, i.e. num0=780, becauce start with 0 will never get a max output.
    def mixmax(self):
        obj=[maxSplit(i,[]) for i in self.numAll()]
        maxAll=[i.multipleMax()[1] for i in obj]
        n=maxAll.index(max(maxAll))
        return obj[n].multipleMax()
num=1200
test1=maxSplit(num,[])
print('test1:',test1.multipleMax())
test2=Mixmaxsplit(num)
print('test2:',test2.mixmax())
