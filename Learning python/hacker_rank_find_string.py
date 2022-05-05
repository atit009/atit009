#!/usr/bin/env python3
def count_substring(string, sub_string):
    count=0
    z=[]
    for i in string:
        if len(sub_string) <=3:   
          z.append(string[count:count+3])
          z.append(string[count:count+2]) 
          z.append(string[count:count+1])
        if len(sub_string) ==4:
            z.append(string[count:count+4])
        if  len(sub_string) ==5:
            z.append(string[count:count+5])
        if  len(sub_string) ==6:
            z.append(string[count:count+6])
        
        count +=1
    c=z.count(sub_string)
    return c 


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)