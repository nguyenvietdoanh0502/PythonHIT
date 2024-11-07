n = int(input('Nhap n: '))
print("Nhap a[]: ")
a = [(input('Nhap: ')) for i in range(n)]
m = int(input('Nhap m: '))
print("Nhap b[]: ")
b = [(input('Nhap: ')) for i in range(m)]
c =[]
for i in range(n):
    if (a[i] in b and not(a[i] in c)):
        c.append(a[i])
print(c)