str=input('Nhap string: ')
res=''
lst=[]
i=0
while(i<len(str)):
    k=0
    if str[i].isnumeric():
        s=''
        
        for j in range(i+1,len(str),1):
            if(str[j]==']'):
                break
            if(str[j]!='['):
                s+=str[j]
        res+=s*int(str[i])
        k=len(s)+2
        lst.append(s)
    elif (str[i-1]==']'):
        s=''
        for j in range(i,len(str),1):
            if(str[j]=='['or str[j].isdigit()):
                break
            s+=str[j]
        res+=s*1
        lst.append(s)
    elif(i==0 and str[i].isalpha()):
        s=' '
        for j in range(i,len(str),1):
            if(str[j]=='['or str[j].isdigit()):
                break
            s+=str[j]
        res+=s*1
        lst.append(s)
    i+=k
    i+=1
print(res)
