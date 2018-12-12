#! /usr/bin/python

import os
import json
import pandas as pd
import numpy as np
import xlwt

def json_r():
#open("D:\Intern\PY\Fourteen.txt",'r',encoding='utf8') as File:
    with open("D:\Intern\PY\city.txt",'r',encoding='utf8') as File:
        f=File.read()
    print(f)
    print(type(f))
    jsonFile=json.load(open(r'D:\Intern\PY\city.txt'))
    print(jsonFile)
    print(type(jsonFile))

    key=list(jsonFile.keys())
    value=list(jsonFile.values())
    myWorkbook=xlwt.Workbook()  #create excel 
    mySheet=myWorkbook.add_sheet("json_string")   #creat a sheet
    #for i in range(len(list(jsonFile.keys())):
    for i in range(len(jsonFile)):
        k1=key[i]
        k2=value[i]
        mySheet.write(i,0,k1)
        mySheet.write(i,1,k2)

    myWorkbook.save('D:\Intern\PY\city.xls')



if __name__=="__main__":
    json_r()

