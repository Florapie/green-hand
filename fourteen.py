import os
import sys
import json
import xlwt

#def json_list_r():
    #kk=open('D:\Intern\PY\Fourteen.txt','r',encoding='UTF-8')
    #jsobj=json.load(kk,encoding='UTF-8')
    #print(jsobj)
    #return jsobj
def json_list_w():
    with open('D:\Intern\PY\Fourteen.txt','r',encoding='utf8') as File: #this student14.txt is edited by myself, the Fourteen.py was copies and only changes the students' name, the wrong display format is because of the initial format.
        f=File.read()
    #print(f)
    f
    if f.startswith(u'\ufeff'): #u means unicode
        #f=unicode(f[3:],'utf8') #py3 don't have unicode function
        #f = f.[3:].decode('utf8') #only "bytes" type can use decode/ has this method, str does not.
        f = f.encode('utf8')[3:].decode('utf8')  #remove first 3 chars
    #print(f)
    f
    text=json.loads(f) #,encoding='UTF-8')
    print(text)
    key=list(text.keys())
    value=list(text.values())

    myWorkbook=xlwt.Workbook()
    mySheet=myWorkbook.add_sheet('value-list')

    for i in range(len(key)):
        k0=value[i]
        mySheet.write(i,0,key[i])
        for j in range(len(k0)):
            k=k0[j]
            mySheet.write(i,j+1,k)
    myWorkbook.save('D:\Intern\PY\Fourteen.xls')


if __name__=="__main__":
    #json_list_r()
    json_list_w()