# /usr/bin/python

'This is exercise-004: calculate number of each character in an English article'

import os
import numpy as np

def char_stat():
    result=dict(zip('abcdefghijklmnopqrstuvwxyz',np.zeros((26,)).astype(int)))
    result['other']=0
    print("initial %s", result)

    with open('D:\Intern\PY\Char.txt','r') as File:
        f=File.read()
    print(f)
    print('total char number: %d' %len(f))
    f=f.lower()
    
    for ch in f:
        if ch in result.keys():
            result[ch]=result[ch]+1
            continue
        else:
            result['other']=result['other']+1
    if sum(result.values())==len(f):
        print("total char: %s, statistical result: %s" %(len(f),result))
    else:
        print('***error***')
        return result
    
if __name__=="__main__":
    char_stat()
