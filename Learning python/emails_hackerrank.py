s=input()
z=[]
for i in s:
    z.append(i)
# print(z)
# print(s)
# a=z.count("a")
# print(a)
b=[]

for i in s:
    if i not in b:
        b.append(i)
# print(b)
b.sort()

for i in b:
    aa=z.count(i)


    print(i,aa)


