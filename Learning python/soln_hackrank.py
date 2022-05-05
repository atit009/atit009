#!/usr/bin/env python3
from itertools import combinations
user=list(map(str,input().split()))
emp=[]
num=int(user[1])
a=user[0]
# print(user)
for i in a:
    emp.append(i)
emp.sort()
# print(emp)
for i in emp:
    print(i)
har=(list(combinations(emp,num)))
out = [item for t in har for item in t]
# print(out)
gopal=(len(out)//2)
j=0
for i in range (gopal):
    c=(out[j:num+j])
    # print(c)
    res = ''.join(map(str, c)) 
    print(res)
    j+=num
