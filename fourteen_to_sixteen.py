import os
import re
import xlwt

def save_xls():
    with open('D:\Intern\PY\student14.txt','r') as file:
        fourteen=file.read()
    with open('D:\Intern\PY\city15.txt','r') as file:
        fifteen=file.read()
    with open(r'D:\Intern\PY\number16.txt','r') as file:
        sixteen=file.read()        
    print(fourteen)
    print(fifteen)
    print(sixteen)

    regexp14=re.compile(r'\"(\d+)\":\[\"([A-Z][a-z]*\s\w*?)\",(\d+),(\d+),(\d+)\]')
    data14=regexp14.findall(fourteen)
    print(data14)
    regexp15=re.compile(r'\"(\d+)\":\"([A-Z][a-z]*)\"')
    data15=regexp15.findall(fifteen)
    print(data15)
    regexp16=re.compile(r'\[(\d+),\s(\d+),\s(\d+)\]')
    data16=regexp16.findall(sixteen)
    print(data16)

    myWorkbook=xlwt.Workbook()
    sheet1=myWorkbook.add_sheet('student14')
    sheet2=myWorkbook.add_sheet('city15')
    sheet3=myWorkbook.add_sheet('numbers16')
    for i in range(len(data14)):
        line=data14[i]
        for j in range(len(line)):
            cell=line[j]
            sheet1.write(i,j,cell)

    for i in range(len(data15)):
        line=data15[i]
        for j in range(len(line)):
            cell=line[j]
            sheet2.write(i,j,cell)

    for i in range(len(data16)):
        line=data16[i]
        for j in range(len(line)):
            cell=line[j]
            sheet3.write(i,j,cell)
    
    myWorkbook.save(r'D:\Intern\PY\fourteen_to_sixteen.xls')


save_xls()