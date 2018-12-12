import os
import xlwt
import json

fileDir='D:\Intern\PY'
def json_r(fileName='number16.txt'):
    with open(os.path.join(fileDir,fileName),'r') as file:
        jsonFile=json.load(file)
    
    print(jsonFile)
    print(type(jsonFile))

    return(jsonFile)

def json_w(jsonFile,fileName='number16.xls'):
    newWorkbook=xlwt.Workbook()
    newSheet=newWorkbook.add_sheet('One')

    for i in range(len(jsonFile)):
        k=jsonFile[i]
        for j in range(len(k)):
            k1=k[j]
            newSheet.write(i,j,k1)
    newWorkbook.save(os.path.join(fileDir,fileName))


# def numbs_w():
#     with open('D:\Intern\PY\shuzi.txt','r',encoding='utf8') as File:
#         f=File.read()
#     print(f)
#     jsonFile=json.loads(f)
    
#     print(jsonFile)


if __name__=='__main__':
    json_w(json_r())