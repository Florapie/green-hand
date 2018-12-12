#! /usr/bin/python

import os
import json
import pandas as pd
import numpy as np
import xlwt

fileDir='D:\Intern\PY'

def json_r(fileName,fileDir='D:\Intern\PY'):
    
    if os.path.isfile(os.path.join(fileDir,fileName)):
        jsonFile=json.load(open(os.path.join(fileDir,fileName)))
        print(jsonFile)
        print(type(jsonFile))
    else:
        print("%s doesn't exist!" %fileName)
    return jsonFile

def json_w(jsonFile,xlsName='city15.xls',sheetName='One'):
    newWorkbook=xlwt.Workbook()  #create excel
    newSheet=newWorkbook.add_sheet(sheetName)  #creat a sheet

    key=list(jsonFile.keys())
    value=list(jsonFile.values())

    for i in range(len(jsonFile)):
        k1=key[i]
        k2=value[i]
        newSheet.write(i,0,k1)
        newSheet.write(i,1,k2)
    newWorkbook.save(os.path.join(fileDir,xlsName))


if __name__=="__main__":
    json_w(json_r('city15.txt'))

