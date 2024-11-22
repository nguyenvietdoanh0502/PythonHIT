dir={}
str= input('Nhap string: ')
for i in str:
    if i not in dir.keys():
        dir[i]=1
    else:
        dir[i]+=1
print(dir)