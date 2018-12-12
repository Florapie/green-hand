import os
import sys
import json
import xlwt
fileDir='D:\Intern\PY'
def main(input='student14.txt',output='student14.xls'):
    with open(os.path.join(fileDir,input),'r') as file:
        jsonFile=json.load(file)  #convert str to type, such as dict, list
    print(jsonFile)
    print(type(jsonFile))

# def json_list_w():
#     with open('D:\Intern\PY\Fourteen.txt','r',encoding='utf8') as File: #this student14.txt is edited by myself, the Fourteen.py was copies and only changes the students' name, the wrong display format is because of the initial format.
#         f=File.read()
#     #print(f)
#     f
#     if f.startswith(u'\ufeff'): #u means unicode
#         #f=unicode(f[3:],'utf8') #py3 don't have unicode function
#         #f = f.[3:].decode('utf8') #only "bytes" type can use decode/ has this method, str does not.
#         f = f.encode('utf8')[3:].decode('utf8')  #remove first 3 chars
#     text=json.loads(f) #,encoding='UTF-8')
#     print(text)
#     print(type(text))
    key=list(jsonFile.keys())
    value=list(jsonFile.values())

    myWorkbook=xlwt.Workbook()
    mySheet=myWorkbook.add_sheet('value-list')

    for i in range(len(key)):
        k0=value[i]
        mySheet.write(i,0,key[i])
        for j in range(len(k0)):
            k=k0[j]
            mySheet.write(i,j+1,k)
    myWorkbook.save(os.path.join(fileDir,output))
main()

# if __name__=="__main__":
#     #json_list_r()
#     json_list_w()