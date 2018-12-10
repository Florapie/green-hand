#！/usr/bin/python

import os

def histogram(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
#        if ch in d():
#            d[ch]+=1
#        else:
#            d[ch]=1
    return d

if __name__=='__main__':
    with open('D:\Intern\PY\Char.txt','r') as File:
        f=File.read()
        f=f.lower()
        print(sorted(histogram(f).items()))

