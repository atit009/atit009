#!/usr/bin/env python3

def average(array):
    a=len(array)
    
    b=sum(array)
    z=b/a
    return z
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
