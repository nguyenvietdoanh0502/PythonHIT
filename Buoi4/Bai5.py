n = int(input('Nhap n: '))
print("Nhap a[]: ")
a = [int(input('Nhap: ')) for i in range(n)]
x = int(input("Nhap x can tim:  "))
a.sort()
left =0
right = len(a)-1
mid = int((left+right)/2)
check=0
while(a[mid]!=x):
    check+=1
    if(a[mid]<x):
        left=mid
    else:
        right=mid
    mid = int((left+right)/2)
    if(check==n):
        mid=-1
        break
print(mid)