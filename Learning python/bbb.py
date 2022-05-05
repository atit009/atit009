#!/usr/bin/env python3
a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
arr=[]
zu=[]
for i in b:
    for j in d:
        if i==j:
            arr.append(i)
        
        
z=set(b)^set(d)

# print(arr)
# print(z)
for i in  z:
    zu.append(i)
print(zu)
print(arr)
atit=zu+arr
print(len(atit))