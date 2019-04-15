#spetial
import datetime
today=datetime.datetime.now()
day=today
delta=datetime.timedelta(days=1)
print(day, delta)

while True:
    day8=f'{day:%Y%m%d}'  #day8=day.strftime('%Y%m%d')
    if len(set(day8)) == 8:
        print(day8)
        break

    day=day-delta

#Friday

year=int(input('input a year: \n'))
#year=2023
days=[datetime.date(year,i,13) for i in range(1,13)]
[print(i) for i in days if f'{i:%a}' == 'Fri']
#black=[print(i) for i in days if f'{i:%a}' == 'Fri']
