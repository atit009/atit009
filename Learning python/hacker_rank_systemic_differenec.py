#!/usr/bin/env python3
from functools import reduce

a=input()
b=list(map(int, input().split()))
# print(b)
c=input()
d=list(map(int, input().split()))

# FIRST_HIGEST=reduce(max,b)
# b.remove(FIRST_HIGEST)
# SECOND_HIGEST=reduce(max,b)
# print(SECOND_HIGEST)
# print(FIRST_HIGEST)
# # print(b)

# FIRST_HIGEST1=reduce(max,d)
# d.remove(FIRST_HIGEST1)
# SECOND_HIGEST1=reduce(max,d)
# print(SECOND_HIGEST1)
# print(FIRST_HIGEST1)

ram=list(set(b)^set(d))
ram.sort()
for i in ram:
    print(i)
        
