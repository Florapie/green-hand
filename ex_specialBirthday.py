import datetime
# 获取今天日期
n_days = datetime.datetime.now()
print(n_days)
while True:
    # 从今天起往前减一天循环
    n_days -= datetime.timedelta(days=1)
    # 获得格式化的时间
    str_time = n_days.strftime('%Y%m%d')
    # 判断数字是否有重复
    if len(set(str_time)) == 8:
        print(str_time)
        break
