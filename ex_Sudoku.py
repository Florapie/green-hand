import numpy as np
class Sudoku(object):
    def __init__(self,N):
        self.N=N
        if self.N % 4 == 0:
            self.num=np.array(range(1,self.N**2+1)).reshape(self.N,self.N)
            print(self.num)
        else:
            self.num=np.zeros((N,N),dtype=np.int)
            #self.num=[i+1 for i in range(N**2)]
    def matric(self):
        def pos(p,q,n=self.N,mat=self.num):
            if 0 <= p-1< n and 0<= q+1 <n:
                if mat[p-1,q+1] == 0:
                    return p-1, q+1
                else:
                    return p+1,q
            elif p-1 <0 and 0<= q+1 < n:
                if mat[n-1,q+1] == 0:
                    return n-1,q+1
                else:
                    return p+1,q
            elif p-1 < 0 and q+1 >= n:
                if mat[n-1,0] == 0:
                    return n-1,0
                else:
                    return p+1,q
            else:
                if mat[p-1,0] == 0:
                    return p-1,0
                else:
                    return p+1,q
        if self.N % 2 == 1:
            for i in range(self.N**2):
                if i==0:
                    p=0
                    q=int((self.N)/2)
                    #print(p,q)
                    self.num[p,q]=i+1 
                    #print(self.num)  
                else:
                    p,q=pos(p,q)
                    #print(p,q)
                    self.num[p,q]=i+1
                    #print(self.num)
            return self.num

        if self.N % 4 == 0:
            print("*********")            
            for i in range(int(self.N/2)):
                self.num[i,i],self.num[self.N-1-i,self.N-1-i]=self.num[self.N-1-i,self.N-1-i],self.num[i,i]
                self.num[i,self.N-1-i],self.num[self.N-1-i,i]=self.num[self.N-1-i,i],self.num[i,self.N-1-i]
            return self.num
            
        if self.N % 2 == 0 and self.N % 4 != 0:
            N1=int(self.N/2)
            num1=np.zeros((N1,N1),dtype=np.int)
            for i in range(N1**2):
                if i==0:
                    p=0
                    q=int((N1-1)/2)
                    num1[p,q]=i+1
                else:
                    p,q=pos(p,q,N1,num1)
                    num1[p,q]=i+1
            addNum=int(self.N**2/4)
            num1=np.vstack((np.hstack((num1,num1+addNum*2)),np.hstack((num1+addNum*3,num1+addNum*1))))
            u=N1
            t=int((self.N-2)/4)
            for j in range(self.N):
                if j < t or j >= self.N-t+1:
                    for i in range(N1):
                        num1[i,j],num1[i+u,j]=num1[i+u,j],num1[i,j]
            num1[t,t],num1[self.N-1-t,t]=num1[self.N-1-t,t],num1[t,t]
            num1[t,t-1],num1[self.N-1-t,t-1]=num1[self.N-1-t,t-1],num1[t,t-1]
            # num1[t-1,0],num1[t+u-1,0]=num1[t+u-1,0],num1[t-1,0]
            # num1[t-1,t-1],num1[t+u-1,t-1]=num1[t+u-1,t-1],num1[t-1,t-1]
            self.num=num1
            return self.num
            # self.num=np.vstack((np.hstack((num1,num1+addNum*2)),np.hstack((num1+addNum*3,num1+addNum*1)))
            # return num1
            # addNum=self.N**2/4
            # #self.num=np.vstack((np.hstack((num1,num1+addNum*2)),np.hstack((num1+addNum*3,num1+addNum*1)))
            # k=np.vstack((np.hstack((num1,num1+addNum*2)),np.hstack((num1+addNum*3,num1+addNum*1)))
            # return 12 #self.num


def calSum(T): #T is np array
    #return sum([T[i,i] for i in range(len(T))])
    return [sum(T[i,:]) for i in range(len(T))] + [sum(T[:,i]) for i in range(len(T))] + [sum([T[i,i] for i in range(len(T))])] + [sum([T[i,len(T)-1-i] for i in range(len(T))])]

# k=4
# T=np.array(range(k**2)).reshape(k,k)
# print(T)
# print(calSum(T))
mat=Sudoku(7)
T=mat.matric()
print(T)
print(calSum(T))

