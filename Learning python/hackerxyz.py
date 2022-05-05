#!/usr/bin/env python3
string="ABCDCDC"
sub_string="CDC"
count=0  
i=0
j=len(sub_string)
for i in range (len(string)):
    if string[i:j]==sub_string:
        count=count+1
    i+=1
    j+=1
    
    
print(count)