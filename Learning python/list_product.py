#!/usr/bin/env python3
from itertools import product
A=input().split()
B=input().split()
a= (list(product(A,B)))
for i in range (len(a)):
    a[i]=int(a[i])
print(a)




