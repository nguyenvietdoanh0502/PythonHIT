s1 = "Chao mung den CLB Tin Hoc HIT"
print(s1)
s2 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT  - 10 diem"
print(s2)
s3 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT "
for i in s3:
    if(i.isupper()):
        print(i,end =' ')
print()
for i in s3:
    if(i.islower()):
        print(i,end = ' ')
print()
s4 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
if(s4.find("CNTT")):
    print("Yes")
else:
    print("No")
for i in s4:
    if(i.isupper()):
        s4 = s4.replace(i,i.lower())
    else:
        s4 = s4.replace(i,i.upper())
print(s4)