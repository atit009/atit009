
arr=[]
a=int(input())
for i in range (a):
    string=input()
    arr.append(string)
# print(arr)
count=1
atit=[]
for i in range (1,len(arr)):
    if arr[0] in arr[i]:
        atit.append(1)
        
    else:
        pass
    count+=1
# print(atit)
ram=len(atit)
# print(len(atit))
ramsharan=[]


for i in range (ram+1):
    ramsharan.append(1)

ramsharan[0]=len(atit)
# print(ramsharan)

# com=combinations("hello",4)
# for i in list(com):
#     print (i)
print(len(atit)+1)
# print(ramsharan)
for i in ramsharan:
    print(i,end=" ")


