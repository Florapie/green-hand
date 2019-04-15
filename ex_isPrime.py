class Prime(object):
    def __init__(self,num):
        self.num=num
    def isPrime(self):
        if self.num <=1 or isinstance(self.num,int) == False:
            print('input number illegal')
        else:
            for i in range(2,self.num):
                if self.num % i == 0:
                    print(self.num, 'is not prime number')
                    break
                else:
                    print(i,'is not facter of',self.num,'try next one')
                    continue
            if i == self.num-1:
                print(f'{self.num} is prime')
 
t=Prime(25)
t.isPrime()




#def isPrime