#!/usr/bin/env python3

o=[]
n = int(input())
s = set(map(int, input().split()))
ran=int(input())
for i in range (ran):
    b=input().split()

    if b[0]=="pop":
        s.pop()
    elif(b[0])=="remove":
        s.remove(int(b[1]))
    elif b[0]=="discard":
        s.discard(int(b[1]))
for i in s:
    o.append(i)

print(sum(o))