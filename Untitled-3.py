import matplotlib.pyplot as plt
import numpy as np

y=lambda x: x**2-2*x+3

x=np.linspace(-1,5,80)


fig1=plt.figure()

ax1=fig1.add_axes([0.1,0.1,0.9,0.9])
ax2=fig1.add_axes([0.35,0.45,0.3,0.25])

ax1.plot(x,y(x),'b-',lw=1.5,label='y')
leg_font={'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
ax1.legend(loc='best',prop=leg_font)
ax1.scatter(1,2,color='',marker='o',edgecolor='g',lw=1.2,s=60)
#legend=plt.legend(prop=leg_font)
ax2.plot(x,np.sin(x))
ax2.set_xticks([])
ax2.set_yticks([])

fig2=plt.figure()
x=lambda t: 16*np.sin(t)**3
y=lambda t: 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
x1=np.linspace(0,2*np.pi,1000)
#x1=np.range(0,2*np.pi,0.001*np.pi)
plt.plot(x1,y(x(x1)),color='r',linewidth=0.75)
plt.title('Heart')
plt.show()

