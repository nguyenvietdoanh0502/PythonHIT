a ={"Doanh","Hieu","Ha","Chien","Vinh","Dung"}
b ={"Doanh","Hieu","Ha"}
x =a-b
print("Cac ban chua check in la: ",x)
print("So ban da dang ky va check in la: ",len(a-x))
k = list(a)
k.sort()
print("Danh sach theo thu tu tang dan: ",k)