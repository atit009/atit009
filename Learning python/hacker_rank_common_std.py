#!/usr/bin/env python3
from posixpath import split


std=int(input())
a=[]
b=[]
for i in range(1,std+1):
    # print(i)
    # a.split()
    a.append(i)
print(a)
std2=int(input())
for j in range (std2):
    gob=input()

# gob=input()
b=gob.split()
# print(a)
# print(b)

gopu=[]
for k in a:
    for l in b:
        if k ==l:
            gopu.append(k)
# print(gopu)
print(len(gopu))
