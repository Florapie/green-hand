import hashlib
import base64
# hashlib.md5, base64 
str0='You are the best'
m=hashlib.md5()
m.update(str0.encode('utf-8'))
out0=base64.encodebytes(bytes(m.hexdigest(),'utf-8'))
# out1=base64.b64encode(m.hexdigest().encode())
print(out0)

def checkString(str0,strList):
    for str1 in strList:
        print('str is: ',str1)
        m1=hashlib.md5()
        m1.update(str1.encode())
        out1=base64.encodebytes(m1.hexdigest().encode())
        if out1 == out0:
            print('RESULT: ',str1)
            break
strList=['I love you',"It's OK",'You are the best']
checkString(str0,strList)