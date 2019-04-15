from sys import argv
def main(f,encoding,error):
    fline=f.readline()
    if fline:
        printLine(fline,encoding,error)
        return main(f,encoding,error)

def printLine(line,encoding,error):
    nextLang=line.strip() #remove head and end, space...
    rawBytes=nextLang.encode(encoding,errors=error)
    cookedLang=rawBytes.decode(encoding,errors=error)
    print(rawBytes,'<====>',cookedLang)

inputEncoding='utf-8' #utf-8
error='ignore' #replacestrict'
f=open('languages.txt','r',encoding=inputEncoding)
main(f,inputEncoding,error)
f.close()