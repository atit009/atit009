#!/usr/bin/env python3
def print_formatted(number):
    for i in range(1,number+1):
        print (i,"", ("{0:o}".format((i))),"",("{0:x}".format(i)) .capitalize(),"" ,("{0:b}".format(i)))

        
    

if __name__ == '__main__':
    n = 2
    print_formatted(n)