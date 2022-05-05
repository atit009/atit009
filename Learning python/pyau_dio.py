# a=int(input())

# zz=[]
# for i in range (a):
#     Mylist=list(map(int,input().split()))
#     zz.append(Mylist)

Atit=[]

for i in range (int(input())):
    try:
        a=list(map(int,input().split()))
        try:
            bal=int(a[0]//a[1])
            Atit.append(bal)
        except  Exception as e:
            Atit.append(f"Error Code: {e}")
    except Exception as e:
        Atit.append(f"Error Code: 3{e}")

    
# print(z)
# print(Atit)
# for i in z:
#     try:
#         Divasable=float(i[0]/i[1])
#         # print(Divasable)
#         Atit.append(Divasable)

#     except Exception as e:
#         Atit.append(f"Error Code : {e}")

# # print(Atit)
# # print(Divasable)
# for i in  Atit:
#     print(i)
for i in Atit:
    print(i)
