import random
choice=['CNTT','KHMT','KTPM','HTTT',"DAPT"]
dir={}
while(True):
    n = int(input('Nhap n: '))
    if(n>=1 and n<=100):
        break
for i  in range(n):
    x=f'Account{i+1}'
    while(True):
        id=input('Nhap MSV: ')
        if(len(id)==10):
            break
    acc={
        'Username ':id,
        'Password':(random.choice(choice)+id)
    }
    dir[x]=acc
print(dir)