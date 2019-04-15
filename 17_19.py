import xlrd
import xml.dom.minidom as md

def readXls(filename):
    book=xlrd.open_workbook(filename)
    sheet1=book.sheet_by_index(0)
    sheet2=book.sheet_by_index(1)
    sheet3=book.sheet_by_index(2)

    name1=sheet1.name
    name2=sheet2.name
    name3=sheet3.name

    d1={}

    for i in range(sheet1.nrows):
        d1[i]=sheet1.row_values(i,1,sheet1.ncols)

    d2={}
    for i in range(sheet2.nrows):
        d2[i]=sheet2.cell_value(i,1)
    d3=[]
    for i in range(sheet3.nrows):
        d3.append(sheet3.row_values(i))  
    return d1,d2,d3



def writeXml(cont1,cont2,cont3):
#    d1,d2,d3=readXls(r'D:\Intern\PY\fourteen_to_sixteen.xls')
    xmlfile1=md.Document()
    rootEle=xmlfile1.createElement('root')
    xmlfile1.appendChild(rootEle)
    subEle=xmlfile1.createElement('student')
    rootEle.appendChild(subEle)

    comment1=xmlfile1.createComment('student\' info table "id" : [name,math,Chinese,English]')
    subEle.appendChild(comment1)

    subCont=xmlfile1.createTextNode(str(cont1))
    subEle.appendChild(subCont)

    with open(r'D:\Intern\PY\student17.xml','wb') as f:
        f.write(xmlfile1.toprettyxml(encoding='utf-8'))

    xmlfile2=md.Document()
    rootEle=xmlfile2.createElement('root')
    subEle=xmlfile2.createElement('cities')
    xmlfile2.appendChild(rootEle)
    rootEle.appendChild(subEle)

    comment=xmlfile2.createComment('city information')
    subEle.appendChild(comment)

    subCont=xmlfile2.createTextNode(str(cont2))
    subEle.appendChild(subCont)

    with open(r'D:\Intern\PY\city18.xml','wb') as f:
        f.write(xmlfile2.toprettyxml(encoding='utf-8'))
    
    xmlfile3=md.Document()
    root=xmlfile3.createElement('root')
    sub=xmlfile3.createElement('numbers')
    xmlfile3.appendChild(root)
    root.appendChild(sub)

    comment=xmlfile3.createComment('number information')
    sub.appendChild(comment)

    cont3=xmlfile3.createTextNode(str(cont3))
    sub.appendChild(cont3)

    with open(r'D:\Intern\PY\numbers19.xml','wb') as f:
        f.write(xmlfile3.toprettyxml(encoding='utf-8'))

d1,d2,d3=readXls(r'D:\Intern\PY\fourteen_to_sixteen.xls')
print("d1:",d1)
print("d2:",d2)
print("d3:",d3)
A= readXls(r'D:\Intern\PY\fourteen_to_sixteen.xls')
print(A)   
print(type(A))  #the return value is tuple
writeXml(d1,d2,d3)



