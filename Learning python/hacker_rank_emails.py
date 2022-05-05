import re
import email.utils

def checker(y):
    pattern=r"^[a-zA-Z0-9-.]+.+@[a-zA-Z]+\.(com|edu|net|moc|az|in)"
    if re.match(pattern,y):
        return  email.utils.formataddr((a[0], y))
    else:
        return " "

n=int(input())
for i in range (n):
    y=input()
    a= email.utils.parseaddr(y)

    print(checker(a[1]))



# import email.utils
# print(type( email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')))
# # print (email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))




