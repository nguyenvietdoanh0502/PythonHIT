a = int(input("Nhap a: "))
c = oct(a)[2:]
check = 0
for i in c :
    if(i==0 and (i+1)!=0):
        break
    elif (i==0):
        check+=1
print("So bit can de bieu dien la: ",(len(c)-check)*3)
#Phan hai
x = dir(a)
print("Danh sach cac thuoc tinh cua va phuong thuc cua kieu du lieu number la: ")
for i in x :
    print(i)