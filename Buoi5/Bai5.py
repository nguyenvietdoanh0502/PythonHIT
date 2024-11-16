dir={
    'version':'3.8',
    'services':'app',
    'image':'python:3.10-slim',
    'command':'python app.py',
    'volumes':'./app:/app',
    'restart':'always',
    'ports':'5000:5000',
    'depends_on':'db'
}
def Print(dir):
    for i in dir.keys():
        print(f'{i}:   {dir[i]}')
Print(dir)
dir['version']='3.10'
Print(dir)
print(f'Image: {dir['image']}')
dir['environment']='PYTHONUNBUFFERED=1'
Print(dir)
print("YES") if 'volumes' in dir.keys() else print("NO")
dir.pop('depends_on')
Print(dir)
print('So luong key trong dir la: ',len(list(dir.keys())))
x = list(dir.values())
print('Tat ca gia tri:')
for i in range(len(x)):
    print(x[i])
print('Co always') if 'always' in dir.values() else print('Khong co always')
key=input('Nhap key: ')
value=input('Nhap value: ')
dir[key]=value
Print(dir)