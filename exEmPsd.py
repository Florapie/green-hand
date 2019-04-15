import re
email='aaa@1234.co9'
psw='Asdfe347ghA'

regex=re.compile("(\w+)@(\w+).(\w+)")
while True:
    mt1=regex.match(email)
    if mt1 == None:
        print('Wrong email, please input a right one: ')
        email=input()
        continue
        
    else:
        print('right email')
        break

while True:
    if re.search(r'[A-Z]',psw) != None and re.search(r'[a-z]',psw) != None and re.search(r'[0-9]',psw) != None:
        print('right code')
        break
    else:
        psw=input()
        continue
    



