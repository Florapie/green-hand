class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender

    
    def setGender(self,gender):
        # if gender == 'male':
        #     self.__gender=gender
        # elif gender =='female':
        #     self.__gender=gender
        # else:
        #     raise ValueError('wrong gender')
        if gender != 'male' and gender != 'female':
            print('Error Gender')
        else:
            self.__gender=gender

    def getGender(self):
        return self.__gender

bart=Student('Bart','male')
bart.setGender('female')
print(bart.name)
print(bart.getGender())
if bart.getGender() != 'female'and bart.getGender() != 'male':
    print('TEST FAILED1')
else:
    bart.setGender('female')
    if bart.getGender() != 'female':
        print('TEST FIALED')
    else:
        print('TEST PASS')
    
