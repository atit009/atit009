#!/usr/bin/env python3
n=int(input())
a=list(map(int,input().split()))
b=int(input())
z=[]
y=[]
for i in range (b):
    details=list(map(int,input().split()))
    if details[0] in a:
        a.remove(details[0])
        z.append(details[1])
    if details[0] not in a:
        y.append(details[1])
# print(details)
# print(a)
print(sum(z))