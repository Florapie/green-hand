import itertools
import numpy as np
def Sudoku(n):
    #[str(i) for i in range(1,n+1)]
    allTuple=itertools.permutations([str(i+1) for i in range(0,n*n)])
    allList=[list(i) for i in allTuple]
    # for i in allList:
        
    #     print(type(np.array(i)),np.array(i))
    for i in allList:
        np1=np.array([int(i1) for i1 in i]).reshape(n,n)
        #[str(i) for i in calSum(np1)]
        print(np1)
        print(calSum(np1))
        if len(set(calSum(np1))) == 1:
            return np1
            break
        #return np1

def calSum(T): #T is np array
    #return sum([T[i,i] for i in range(len(T))])
    return [sum(T[i,:]) for i in range(len(T))] + [sum(T[:,i]) for i in range(len(T))] + [sum([T[i,i] for i in range(len(T))])] + [sum([T[i,len(T)-1-i] for i in range(len(T))])]

# k=4
# T=np.array(range(k**2)).reshape(k,k)
# print(T)
# print(calSum(T))
print(Sudoku(3))
