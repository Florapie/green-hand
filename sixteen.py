import os
import xlwt
import json

def numbs_w():
    with open('D:\Intern\PY\shuzi.txt','r',encoding='utf8') as File:
        f=File.read()
    print(f)
    jsonFile=json.loads(f)
    
    print(jsonFile)


if __name__=='__main__':
    numbs_w()