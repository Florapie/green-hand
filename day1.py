import os
import math

###################1
def bubble(a):
    for i in range(len(a)-1,-1,-1):
        for j in range(len(a)-1,len(a)-1-i,-1):
            if a[j]>a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]

    return a

def selection(a):
    lenth=len(a)
    for i in range(len(a)):
        m=min(a[:len(a)-i])
        #n=a.index(min(a[:len(a)-i]))
        a.remove(m)
        a.insert(len(a)-i,m) #the last command makes a 1 shorter
        #a.append(m) #this would range from smallest to largest
    return a

def insert(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                b=a[i]
                a[i]=a[j]
                a[j]=b
    return a
a=[8,2,4,6,1,9,0,3,5,7]
print("bubble result:",bubble(a))
print("selection result:",selection(a))
print("insert result:",insert(a))

a.sort(reverse=True)  #reverse range
print('simple way:',a)

###################2
def y(x):
    y=x**(x/3)
    return y
def y1(x):
    y1=y(x)*(math.log(x)+1)/3
    return y1

def find_ini(a,b):
    ya=y(a)-2
    yb=y(b)-2
    while ya*yb > 0:
        b=eval(input('Please input another b:'))
        yb=y(b)
    return a,b   

def bisection(a,b):
    c=0.5*(a+b)
    y3=y(c)-2
    # print(" a=%.6f,  b=%.6f,  c=%.6f" %(a,b,c))
    # print("fa=%.6f, fb=%.6f, fc=%.6f" %(y(a)-2,y(b)-2,y3))

    while abs(y3)>0.001:
        c=0.5*(a+b)
        y3=y(c)-2
        print(" a=%.6f,  b=%.6f,  c=%.6f" %(a,b,c))
        print("fa=%.6f, fb=%.6f, fc=%.6f" %(y(a)-2,y(b)-2,y3))
        if (y(a)-2)*(y(c)-2)>0 and (y(b)-2)*(y(c)-2)<0:
            a=c
        elif (y(a)-2)*(y(c)-2)<0 and (y(b)-2)*(y(c)-2)>0:
            b=c
        else:
            c="ERROR" # How to raise error?
    #     if abs(y3) > 0.001:
    #     if (y(a)-2)*(y(c)-2)>0 and (y(b)-2)*(y(c)-2)<0:
    #         a=c
    #     elif (y(a)-2)*(y(c)-2)<0 and (y(b)-2)*(y(c)-2)>0:
    #         b=c
    #     else:
    #         c='ERROR'
    #     bisection(a,b)
    if abs(y(a)-2)<=abs(y(b)-2):
        return a,y(a)
    else:
        return b,y(b)
 
        

def main1(a0,b0):
    y_a=y(a0)-2
    y_b=y(b0)-2
    print("y_a=%.3f, y_b=%.3f" %(y_a,y_b))
    a,b=find_ini(a0,b0)
    print("a=%.3f, b=%.3f" %(a,b))
    return bisection(a,b)
#X1,Y1=main1(0,3)
#print("x=%.6f, result=%.6f" %(X,Y))

def Newton(x):
    fx=y(x)-2
    fx1=y1(x)
    z=x-fx/fx1
    return z

def main2(x): 
    print("x=%f" %x)
    while abs(y(x)-2)>0.001:
        x=Newton(x)
        print("x=%f" %x)
    return x
#X2=main2(eval(input("please input initial x:")))
#print("Newton result: x=%f, y=%f" %(X2,y(X2)))

##################3
def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
#print(Fibonacci(eval(input('Please input an integer: '))))