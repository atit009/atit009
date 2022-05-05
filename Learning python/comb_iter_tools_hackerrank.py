#!/usr/bin/env python3
from itertools import combinations
y=[]
a=list(map(str,input().split()))
# print(a[0])
z=a[0]
for i in (z):
    y.append(i)
y.sort()
# print(y)
for i in y:
    print(i)
har=(list(combinations(y,3)))
# print(har)
# print(type(har))

out = [item for t in har for item in t]
print(out)
