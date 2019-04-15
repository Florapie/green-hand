class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1

if Student.count != 0:
    print('TEST FAIL')
else:
    bart1=Student('Bart')
    if Student.count != 1:
        print('TEST FAIL')
    else:
        bart2=Student('Bart')
        if Student.count != 2:
            print('TEST FAIL')
        else:
            print('TEST PASS')
    
            
