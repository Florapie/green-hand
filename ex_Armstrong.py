for i in range(1001):
    s=list(str(i))
    result1=sum([int(s[k0])**3 for k0 in range(len(s))])
    if result1 == i:
        print(i)
        #return i
    