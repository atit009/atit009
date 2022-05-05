#!/usr/bin/env python3
from pickle import NONE


z=[]
a="-"
b=".|."
ram=input().split()
LENGTH=(int(ram[0]))
WEIGHT=(int(ram[1]))
COUNT=1
DROP=3
CHANDRA=(LENGTH-1)//2
KAJI=(WEIGHT-7)//2
# ATIT=b*COUNT
# TOTAL=WEIGHT
# ATTACH=WEIGHT-DROP
COUNT1=0
for i in range(1,CHANDRA+1):
    ATIT=((a*((WEIGHT-DROP-COUNT1)//2)+(b*COUNT)+(a*((WEIGHT-DROP-COUNT1)//2))))
    z.append(ATIT)
    print(ATIT)
        
    DROP +=3
    COUNT +=2
    COUNT1 +=3
# print(z)
print((a*KAJI)+"WELCOME"+(a*KAJI))
ANJAN=3
PAE=3
for i in range(1,CHANDRA+1):
    print((a*PAE)+b*((WEIGHT-ANJAN-ANJAN)//3)+a*PAE)
    PAE +=3
    ANJAN +=3
        
    