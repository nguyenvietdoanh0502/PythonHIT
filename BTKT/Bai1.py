def GT(x):
    sum=1
    for i in range(1,x+1,1):
        sum*=i
    return sum
x= int(input('Nhap x:  '))
res=1+x
for i in range(2,1000,1):
    res+=(x**i)/(GT(i))
print(f'E mu {x} = {res}')