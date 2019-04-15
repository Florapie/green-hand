import numpy as np

def rotate(matrix):
    if matrix == [[]]:
        return matrix
    else:
        matT=np.transpose(np.array(matrix))
        a=sorted([i for i in range(len(matrix))],reverse=True)
        mat1=matT[:,a] #only metrix can exchange row or col so easy, nxn list can't
        return mat1.tolist()
        #return zip(*matrix[::-1]) #just this one line can do the work
    
if __name__=="__main__":
    m1 = [[]]
    m2 = [[1]]
    m3 = [[i for i in range(3)] for j in range(3)]
    m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    assert rotate(m1) == [[]]
    assert rotate(m2) == [[1]]
    #print([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    assert rotate(m4) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]