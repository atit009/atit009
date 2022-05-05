#!/usr/bin/env python3
def print_rangoli(size):
    size=(n*4)-3
    ek_total=(size-1)//2
    atit=0
    count=0   
    blank="-"
    Alphabet="-abcdefghijklmnopqrstuvwxyz"
    for i in range (n-1):
        print(blank*(ek_total-atit)+Alphabet[n-count]+blank*ek_total+blank*atit)
        count +=1
        atit +=2
    
if __name__ == '__main__':
    n = 5
    print_rangoli(n)