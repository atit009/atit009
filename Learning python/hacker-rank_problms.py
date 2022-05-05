#!/usr/bin/env python3
# y=[]
# a="abracadabra"
# for i in a:
#     y.append(i)
# print(y)
# inp=4
# z=y[inp]
# p="k"
# av=a.replace(z,p)
# print(av)
# a="Atit is a good boy .Atit is nice"
# y=a.split()
# y[0]="Appu"
# z=a.replace(y[0],)
# print(z)
# print(y)
y=[]
string="abracadabra"
position="5"
character="k"
for i in string:
    y.append(i)
y[int(position)]=character
z="".join(y)
print(z)