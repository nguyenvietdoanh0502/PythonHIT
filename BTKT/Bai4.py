data = [
    "name=Alice;age=30;score=85.5" ,
    "name=Bob;age=25;score=90" ,
    "name=Alice;age=30;score=92" ,
    "city=NewYork;name=Eve;age=35;score=88" ,
    "city=London;name=Alice;age=30;score=85.5"
]
lst=[]
for i in data:
    lst+=i.split(';')
print(lst)
lst2=[]
for i in lst:
    lst2+=i.split('=')
print(lst2)
dict={

}
