#!/usr/bin/env python3
from itertools import combinations_with_replacement
z=[]
a=input().split()
for i in (a[0]):
    z.append(i)
z.sort()
# print(z)
b=(list(combinations_with_replacement(z,int(a[1]))))
for i in b:
    i=list(i)
    b=''.join(i)
    print(b)
