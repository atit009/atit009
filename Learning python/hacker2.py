#!/usr/bin/env python3
a=int(input())
az=input()
har=az.split()
b=int(input())
bz=input()
bar=bz.split()
# print(har)
# print(bar)
har=[int(i) for i in har ]
bar=[int(i) for i in bar]
# print(har)
# print(bar)
gopu=[]
for z in har:
    for ap in bar:
        if z==ap:
            gopu.append(z)
# print(gopu)
print(len(gopu))

