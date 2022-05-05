# a=set(list(map(int,input().split())))
# b=set([1,2,3,4,5,6,7])
# print(set(a-b))
z=[]
a=int(input())
b=set(list(map(int,input().split())))
c=int(input())
d=set(list(map(int,input().split())))
zz=(set(b^d))
# print(zz)

for i in zz:
    z.append(i)
print(len(z))