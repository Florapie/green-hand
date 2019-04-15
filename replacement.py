import os
import re
with open(r'D:\Work\Model\pyInput\personal_information.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        if line.startswith("Mobil"):
            regex=re.compile('^Mobil:\s\d{3}(\d{4})\d{4}')
            res=regex.search(line).groups()
            print("before",res)
            print(type(res))
            line1=re.sub(res[0],"****",line)
            print('after',line1)
            line2=line.replace(res[0],"****")
            print('after',line2)
            print(type(line1),type(line2))
            # res1=re.search(regex,line).groups()
            # print("res1",res1)



    f1=f.read()
    print(type(f))
    print(type(f1))
    print(f1)

def filt(oriFile):
    info1="ID number"
    info2="Mobil"
    fileData=""
    with open(oriFile,'r') as file:
        for line in file:
            if line.startswith(info1):
                print("line1",line)
                line1=list(line)
                line1[-13:-4]=['*','*','*','*','*','*','*','*','*','*']
                line2=''.join(line1)
                fileData+=line2
                #re.sub(r'^info1\d{6}')
            elif line.startswith(info2):
                print("line2",line)
                line1=list(line)
                line1[-8:-5]=['*','*','*','*']
                line2=''.join(line1)
                fileData+=line2
            else:
                fileData+=line
    print(fileData)
    with open(r'D:\Work\Model\pyInput\personal_information_replace.txt','w') as newF:
        newF.write(fileData)

#oriFile=r'D:\Work\Model\pyInput\personal_information.txt'
#filt(oriFile)
        
