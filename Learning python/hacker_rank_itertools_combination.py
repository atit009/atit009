#!/usr/bin/env python3
from itertools import combinations
a=input().split()
z=[]
b=a[0]
for i in b:
    z.append(i)
# print(z)
z.sort()
for i in z:
    print(i)
# print(z[0:(int(a[1])*3)])
c= (list(combinations(z,int(2))))
# print(c)
zc=(int(a[1])*2)
# print(zc)
m=(c[0:zc])
for i in m:
    b=''.join(i)
    print(b)
    print(i)