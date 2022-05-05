z=[]
zz=[]
count=0
a=int(input())
for i in range (a):
    phone_num=(input())
    z.append(phone_num)
# print(z)
for i in range (a):
    for i in z[0+count]:
        zz.append(i)
    count+=1
print(zz)
if zz[0]==("9" or "8" or "7"):
    print("YES")
else:
    print("NO")
# print(zz[10])
if zz[10]==("9" or "8" or "7"):
    print("YES")
else:
    print("NO")

# print(len(zz))
if len(zz)>=29:
    print("NO")