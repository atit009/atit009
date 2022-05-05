#!/usr/bin/env python3
n=int(input())
banana=[]
potato=[]
apple=[]
candy=[]
for i in range (n):
    fruits=list(map(str,input().split()))
    if fruits[0]=="BANANA":
        s1=fruits[0]+" "+fruits[1]
        banana.append(fruits[2])
        
    elif fruits[0]=="POTATO":
        s2=fruits[0]+" "+fruits[1]
        potato.append(fruits[2])
    elif fruits[0]=="APPLE":
        s3=fruits[0]+" "+fruits[1]
        apple.append(fruits[2])
    elif fruits[0]=="CANDY":
        s4=fruits[0]
        candy.append(fruits[1])

# print(s1 )

banana=[int(i) for i in banana]
potato=[int(i)for i in potato]
apple=[int(i)for i in apple]
candy=[int(i)for i in candy]
print(s1 , sum(banana))
print(s2, sum(potato))
print(s3, sum(apple))
print(s4, sum(candy))
# print(potato)
# print(apple)
# print(candy)
# print(banana)