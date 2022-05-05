#!/usr/bin/env python3

def print_rangoli(size):
    size=n*4-3
    b=[]
    Alphabet=[]
    Alphabet1="-abcdefghijklmnopqrstuvwxyz"
    for i in (Alphabet1):
        Alphabet.append(i)
    # print(Alphabet)


    z='-'*size
    yy=z.replace(z[n],Alphabet[n])
    # print(yy)
    Alphabet[n]=z[n-1]
    for i in z :
        b.append(i)
    b[n]=Alphabet[n-1]
    # print(b)
    for i in (b):
        print(i , end='')
    

if __name__ == '__main__':
    n = 5
    print_rangoli(n)