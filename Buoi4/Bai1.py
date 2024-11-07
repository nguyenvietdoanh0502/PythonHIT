k = int(input("Nhap k: "))
lst= [(int(input("Nhap: "))) for i in range(k)]
print (lst)
n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
if(m*n>k):
    print('Khong the xay dung ma tran')
else:
    index = 0
    mt = []
    for i in range(n):
        dong=[]
        for i in range(m):
            dong.append(lst[index])
            index+=1
        mt.append(dong)
print(mt)