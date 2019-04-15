class Year(object):
    def __init__(self,year):
        self.year=year
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    def dayCount(self):
        if self.year % 100 != 0:
            if self.year % 4 == 0:
                return 366
            else:
                return 365
        else:
            if self.year % 400 == 0:
                return 366
            else:
                return 365
    
    def monthDay(self):
        if self.dayCount() == 366:
            self.month[1]=29
            return self.month
        else:
            return self.month


def main(year):
    diffY=year-2017
    listY=list(range(2017,year))
    yearDate=[]
    monthDay=[]
    for i in range(2017,year):
        inputYear=Year(i)
        yearDate.append(inputYear.dayCount())
    daySum=sum(yearDate)
   
    year1=Year(year)
    month1=year1.monthDay()
    diffTot=[]
    result=[]
    for j in range(len(month1)):
        diffTot.append(daySum+sum(month1[:j])+12)
    
    for k in range(len(diffTot)):
        if diffTot[k]%7 == 5: #difference is 5 days, i.e. Friday
            outStr='-'.join([str(year1.year),str(k+1),'13'])
            result.append(outStr)
        #else:
        #   return result
    return result


print('Black Friday: >\n',main(2023))        
    
# from datetime import date
# year = int(input('inquire year: '))
# days = [date(year, i, 13) for i in range(1, 13)]
# fridays = [str(i) for i in days if f'{i:%a}' == 'Fri']
# print('Black Friday:\n{}'.format("\n".join(fridays)))
