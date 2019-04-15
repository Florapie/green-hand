import pandas as pd
import numpy.random as npr
import matplotlib.pyplot as plt
import datetime
import statsmodels.api as sm
import scipy.stats as scs

X=npr.standard_normal((5000))
Y=npr.normal(1,4,(5000))
Z=npr.uniform(-3,3,(5000))
W=npr.lognormal(0,1,(5000))

fig=plt.figure()
sub1=fig.add_subplot(2,2,1)
sub2=fig.add_subplot(2,2,2)
sub3=fig.add_subplot(2,2,3)
sub4=fig.add_subplot(2,2,4)
bin=500
sub1.hist(X,bin)
sub1.set_title('standard normal')
sub2.hist(Y,bin)
sub2.set_title('normal')
sub3.hist(Z,bin)
sub3.set_title('uniform')
sub4.hist(W,bin)
sub4.set_title('log normal')


# fig2=plt.figure()
# sub2_1=fig2.add_subplot(2,2,1)
# sub2_2=fig2.add_subplot(2,2,2)
# sub2_3=fig2.add_subplot(2,2,3)
# sub2_4=fig2.add_subplot(2,2,4)

# plt.subplot(2,2,1)
sm.qqplot(X)
plt.title('standard normal')
sm.qqplot(Y)
plt.title('normal')
sm.qqplot(Z)
plt.title('uniform')
sm.qqplot(W)
plt.title('log normal')
# plt.subplot(2,2,2)
# sm.qqplot(Y)



print('Skew: %f' %scs.skew(X))
print('Skew: %f' %scs.skew(Y))
print('Skew: %f' %scs.skew(Z))
print('Skew: %f' %scs.skew(W))
print('kurtosis: %f' %scs.kurtosis(X))
print('kurtosis: %f' %scs.kurtosis(Y))
print('kurtosis: %f' %scs.kurtosis(Z))
print('kurtosis: %f' %scs.kurtosis(W))
print('Skew test: %f' %scs.skewtest(X)[1])
print('Skew test: %f' %scs.skewtest(Y)[1])
print('Skew test: %f' %scs.skewtest(Z)[1])
print('Skew test: %f' %scs.skewtest(W)[1])
print('Normal test: %f' %scs.normaltest(X)[1])
print('Normal test: %f' %scs.normaltest(Y)[1])
print('Normal test: %f' %scs.normaltest(Z)[1])
print('Normal test: %f' %scs.normaltest(W)[1])

plt.show()
# web.get_data_yahoo('AAPL')
# FT=data.DataReader('GOOG',data_source='yahoo',start='2000-1-1')
# #FT=data.DataReader(name='^FTSE',data_source='yahoo',start='2000-1-1')
# print(FT.info())
# print(FT.tail())
# FT['Close'].plot(figsize=(8,6),grid=True)

# start = datetime.datetime(2016, 1, 1) # or start = '1/1/2016'
# end = datetime.date.today()
# prices = web.DataReader('AAPL', 'yahoo', start, end)
# print(prices.head())  # print first rows of the prices data
# from pandas_datareader import data as pdr
 
# import fix_yahoo_finance as yf
# yf.pdr_override() #需要调用这个函数
 
# # 获取数据
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
# data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")