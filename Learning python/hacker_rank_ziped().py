#!/usr/bin/env python3
# a=zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
# print(zip([1,2,3,4,5,6],'Hacker'))
# print(list(a))
z=[]
a=list(map(int,input().split()))
for i in range (a[1]):
    inp=list(map(float,input().split()))
    z.append(inp)
# print(z)
hh=(list(zip(*z)))
# print(list(zip(z)))
for i in hh:
    print(sum(i)/a[1])
