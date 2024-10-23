a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a//b =",a//b)
print("a**b = ",a**b)
print("a/b = ",a/b)
if(a==b):
    print("a=b")
else:
    if(a<b):
        print("a<b")
    else:
        print("a>b")
print("a AND b: ", a & b)
print("a or b: ",a | b)
print("a XOR b: ",a ^ b )
print("NOT a==b: ",~ a==b)
print("a>>5 = ", a>>5)
print("a<<5 = ", a<<6)
x = bin(a)[2:]
y = x[::1]
print("He co so 2 dao nguoc cua a=",y)