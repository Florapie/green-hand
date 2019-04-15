import numpy as np
import scipy as sp
from scipy import integrate,optimize,stats

a=np.arange(20)
a1=a.reshape((4,5))
a2=a.reshape((-1,4))
b=np.dot(a1,a2)
print(a1)
print(a2)
print(b)

def f(x):
    return np.sin(x+1)/np.exp(x)*(x+1)/2

x=np.random.rand(5)
y=f(x)
print(x)
print(y)

m=np.linspace(0,1,1001)
dm=m[1]-m[0]
n1=sum(f(m)*dm)

n2,error2=integrate.quad(f,0,1)
print(n1)
print(n2,error2)

def y1(x):
    return x**(x/3)-2
x1=optimize.newton(y1,1)
x2=optimize.bisect(y1,0,3)

print(x1,x2)

# y0=lambda x: np.exp(-x**2/2)
# N=1/(2*np.pi)**0.5*integrate(y0(x),-float('inf'),x)
d1=lambda S,K,T,r,sigma: (np.log(S/K)+(r+sigma**2/2)*T)/sigma*T**0.5
d2=lambda S,K,T,r,sigma: (np.log(S/K)+(r-sigma**2/2)*T)/sigma*T**0.5

def C0(S,K,T,r,sigma):
    d_1=d1(S,K,T,r,sigma)
    d_2=d2(S,K,T,r,sigma)
    N_1=stats.norm.cdf(d_1)
    N_2=stats.norm.cdf(d_2)

    C0=S*N_1-K*np.exp(-r*T)*N_2
    return C0

print('result:',C0(1,1,1,1,1))