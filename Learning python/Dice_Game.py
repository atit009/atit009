from functools import reduce
# a=[1,2,3,4]
# print(reduce(max,a))

z=[]
a=list(map(int,input().split()))
for i in range (a[0]):
    b=list(map(int,input().split()))
    z.append(b)

# print(z)
atit=[]
for i in z:
    goppal=reduce(max,i)
    atit.append(goppal)
Ramsharan=[]
# print(atit)
for i in atit:
    Ramsharan.append(i*i)

# print(Ramsharan)

ouranswer=sum(Ramsharan)%a[1]
print(ouranswer)
    









