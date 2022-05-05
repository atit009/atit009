#!/usr/bin/env python3
from itertools import permutations
from itertools import combinations

a=input().split()
a.sort()
b=a[1]
z=[]
y=[]
for i in b:
    
    z.append(i)
z.sort()
# print(z)
# print(a[0])
c=(list(permutations(z,int(a[0]))))
# print(c)

hh=0
if int(a[0])==1:
    hh=1
for i in c:
    if int(a[0])==1:
        print(i[0])
    if int(a[0])==2:
        print(i[0]+i[1])
    if int(a[0])==5:
        print(i[0]+i[1]+i[2]+i[3]+i[4])
    if int(a[0])==3:
        print(i[0]+i[1]+i[2])
    if int(a[0])==4:
        print(i[0]+i[1]+i[2]+i[3])
    # else:
    
    #     # print(i[1])
    #     # print(i)
    #     print(i[0]+i[1])
    # else:
    #     print(i[0])

    






# a=["a","t","i","t"]
# a.sort()
# print(a)
# # z=[]
# a=input().split()
# a.sort()
# a[1].sort()
# print(a)

# b=a[0].sort()
# # print(a)
# # print(z)
# print(list(permutations(b[0],int(a[-1]))))