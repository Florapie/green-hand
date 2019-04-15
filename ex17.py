from sys import argv
from os.path import exists

#1.read file, truncate, and rewrite
#2.one input file, one output file, write input to output.
script,reFile,inFile,outFile=argv
#reFile=ex17_test.txt, inFile=ex17_in.txt,outFile=ex17_out.txt
print(f'We are runing {script}, reading {reFile}, adding {inFile} to {outFile}')
#reFile="test.txt"
f1=open(reFile,'r+',encoding='utf-8')
f1Txt=f1.read()
print("***Ori txt***\n",f1Txt)

#f1.seek(0,0) #r+ location is end
f1.truncate(6) #keep the first N chars
f1.seek(0,0)
print("After truncate:\n",f1.read())  #from current position to the end, not the final text content
## print("read2_f1\n",f1.read()) #this line will show nothing because of the end location.
addLine1=input('input line 1: ')
addLine2=input('input line 2: ')

#f1.write(addLine1,"\n",line2,"\n")
f1.write(addLine1)
f1.write("\n")
f1.write(addLine2)  #how write all lines in one command sentense
f1.write("\n")
f1.seek(0,0)
print("***fin_reFile***\n",f1.read())
f1.close()

f2=open(inFile,'r')
f3=open(outFile,'a+')
f3.write(f2.read())
#f2.seek(0,0)
print('***inFile***\n',f2.read())
#print('***outFile***\n',f3.read())

f3.seek(0,0)
print('***fin_outFile***',f3.read())
f2.close()
f3.close()
