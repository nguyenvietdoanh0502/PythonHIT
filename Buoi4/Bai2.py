n = int(input('Nhap n: '))
print("Nhap a[]: ")
a = [(input('Nhap: ')) for i in range(n)]
m = int(input('Nhap m: '))
print("Nhap b[]: ")
b = [(input('Nhap: ')) for i in range(m)]
c = []
for i in range(max(n,m)):
    if i < n:
        c.append(a[i])
    if i< m:
        c.append(b[i])
print (c)
