#!/usr/bin/env python3
def average(arr):
    z=[]
    a=arr
    for i in a:
        for j in a:
            if i==j:
                a.remove(i)
            if i !=j:
                z.append(i)
    for i in z:
        for j in z:
            if i==j:
                z.remove(i)
    har=arr+z
    print(har)
    lenu=len(har)
    summ=sum(har)
    avg=summ/lenu
    return avg
  

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)