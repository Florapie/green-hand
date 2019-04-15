def PaskaRow(M): # M is the row number
    # l=[]
    # row=[]
    if M == 0:
        #row = [1]
        #l.append([num])
        return [1]
    elif M == 1:
        #row = [1,1]
        #l.append([1,1])
        return [1,1]
    else:
        row1=[1]
        row0=PaskaRow(M-1)
        for i in range(len(row0)-1):
            row1.append(row0[i]+row0[i+1])
        #[row0[i]+row0[i+1] for i in range(len(row0)-1)]
        row1.append(1)
        #row=row1
        return row1

def PaskaNum(M,N):
    row0=PaskaRow(M)
    return (row0[N])

def PaskaTriangle(height):
    for i in range(height):
        print(PaskaRow(i))
print(PaskaRow(6))
print(PaskaNum(3,2))
PaskaTriangle(5)