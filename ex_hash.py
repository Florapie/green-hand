import hashlib

def hashFile(hashType,file):
    hashArgo=hashlib.new(hashType)
    readSize=1024*1024
    with open(file,'r',encoding = 'utf-8') as f:
        while True:
            f1=f.read(readSize)
            if f1:
                hashArgo.update(f1.encode('utf-8'))
            else:
                break   
    return hashType,hashArgo.hexdigest()

if __name__=='__main__':
    print(hashFile('md5','ex_hash.txt'))
