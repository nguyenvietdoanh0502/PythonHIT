n = int(input('Nhap n:  '))
dir = {}
for i in range(n):
    key=input("Nhap key:  ")
    value=input("Nhap value:  ")
    dir[key]=value
print(dir)
dir2={}
for i in dir.keys():
    if dir[i] in dir2.keys():
        dir2[dir[i]]="None"
    else:
        dir2[dir[i]]=i
print(dir2)
