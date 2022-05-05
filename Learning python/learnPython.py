atit=[]

a=int(input())
for i in range (a):
    try:
        bb=float(input())
        if bb==0:
            atit.append("False") 
        else:
            atit.append("True")

    except:
        atit.append("False")


print(atit)

for i in atit:
    print(i)

    


