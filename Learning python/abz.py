#!/usr/bin/env python3
from itertools import combinations
a=["H","A","C","K"]
# a=list(map(str,input().split()))
z=2
a.sort()
b=a[0]
har=(list(combinations(a,3)))
out = [item for t in har for item in t]
# print(har)
har=(len(out))
gopal=har//2
print(gopal)
j=0
for i in range(gopal):
    c=(out[j:z+j])
    # print(c)
    res = ''.join(map(str, c)) 
    print(res)
    j+=z
