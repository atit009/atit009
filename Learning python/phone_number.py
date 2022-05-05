import re

def checker(y):
    pattern=r"^[7,8,9]\d{9}$"
    if re.match(pattern,y):
        return "YES"
    else:
        return "NO"




a=int(input())
for i in range (a):
    y=input()
    print(checker(y))