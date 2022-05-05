import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
z=[]
x=[]
y=[]

a=list(map(int,input().split()))
count=0
count1=3
count2=6
for i in range (3):
    z.append(a[count])
    x.append(a[count1])
    y.append(a[count2])
    count1+=1
    count2+=1
    count+=1



a=np.array([z,x,y])
print(a)
# print(z)
# print(x)
# print(y)