import numpy as np
class Rome(object):
    def __init__(self,romeNumber,pick={'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}):
        self.romeNumber=romeNumber
        self.pick=pick
        #self.pick={'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}
    #def exchange(self,romeNumber):
    def exchange(self):
        romeStr=list(str(self.romeNumber))
        print(romeStr)
        k=[int(i) for i in list(np.ones(len(romeStr)))]
        # print(k)
        # k[0]=-1
        # print(k)
        if len(romeStr)==1:
            return self.pick[romeStr[0]]
        else:
            
            k1=[i for i in range(len(romeStr)-1) if romeStr[i] in 'IXC' and self.pick[romeStr[i]] < self.pick[romeStr[i+1]]]
            for i in k1:
                k[i]=-1
            return sum([self.pick[romeStr[i]]*k[i] for i in range(len(romeStr))])
        # elif romeStr[0] in 'IXC' and self.pick[romeStr[0]] < self.pick[romeStr[1]]:
        #     res=sum([self.pick[romeStr[i]] for i in range(1,len(romeStr))])-self.pick[romeStr[0]]
        #     return res
        # else:
        #     res=sum([self.pick[romeStr[i]] for i in range(len(romeStr))])
        #     return res



class reverseRome(object):
    def __init__(self,number,pick={'1':'I','10':'X','100':'C','1000':'M','5':'V','50':'L','500':'D'}):
        self.__number=number
        self.pick=pick
    def getNumber(self):
        return self.__number
    def setNumber(self,number):
        if 0< number < 4000:
            self.__number=number
        else:
            raise ValueError("range is (0,4000)")
    def single(self,num,dkt):
        if num == 5:
            return dkt[1]
        if num > 5:
            return dkt[1]+dkt[0]*(num-5)
        if num == 4:
            return dkt[0]+dkt[1]
        if num < 4:
            return dkt[0]*num
    def exchange(self):
        intStr=list(str(self.__number))
        intSingle=[int(i) for i in intStr]
        print(intSingle)
        dict0={0:'I',1:'V'}
        dict1={0:'X',1:'L'}
        dict2={0:'C',1:'D'}
        if len(intSingle) == 4 and intSingle[0] < 4:
            return 'M'*intSingle[0]+self.single(intSingle[1],dict2)+self.single(intSingle[2],dict1)+self.single(intSingle[3],dict0)
        if len(intSingle) == 3:
            return self.single(intSingle[0],dict2)+self.single(intSingle[1],dict1)+self.single(intSingle[2],dict0)
        if len(intSingle) == 2:
            return self.single(intSingle[0],dict1)+self.single(intSingle[1],dict0)
        if len(intSingle) == 1:
            return self.single(intSingle[0],dict0)

#a=Rome(input('please input a Rome str:\n'))
a=Rome('XIX')
print(a.exchange())
# b=reverseRome(14)
# print(b.getNumber())
# print(b.pick)  
# print(b.exchange())     


