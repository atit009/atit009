#!/usr/bin/env python3
def average(array):
    b=(set(array))
    z=[]
    for i in b:
        z.append(i)
    summ=sum(z)
    lenn=len(z)
    avg=summ/lenn
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)