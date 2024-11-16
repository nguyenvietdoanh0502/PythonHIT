n = int(input("Nhap n: "))
a = tuple([int(input()) for i in range(n)])
b = tuple([input() for i in range(n)])
x = [i for i in a if (i>sum(a)/len(a))]
print("So luong phan tu la: ",len(x))
A = tuple([i for i in a if(i%2==0)])
B = tuple([i for i in a if(i%2!=0)])
print("Tuple chan: ",A)
print('Tuple le: ',B)
k = input("Nhap K: ")
check=0
for i in b:
    if k in i:
        check+=1
print("So luong phan tu k trong B la: ",check)
check2=0
for i in b:
    if(len(i)>5):
        check2+=1
print("So luong phan tu dai hon 5 la: ",check2)
d=[]
for i in range(len(a)):
    xx=tuple([a[i],b[i]])
    d.append(xx)
c = tuple(d)
print(c)