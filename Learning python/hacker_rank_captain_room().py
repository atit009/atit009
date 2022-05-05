#!/usr/bin/env python3
arr = [1 ,2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
dic = {}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]= 1
print(dic)
for i in dic:
    if dic[i] == 1:
        print(i)