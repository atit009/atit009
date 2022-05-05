z=[]
a=int(input())

for i in range (a):
    b=int(input())
    listed=list(map(int,input().split()))
    z.append(listed)
    
print(z)


for i in z:
    print(i)