# atit=0
# a=["9851042091","823530761"]
# for i in range (len(a)):
#     print(a[atit][0])
#     atit+=1
atit=0
alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a=int(input())
zz=[]
sharma=[]
for i in range (a):
    phone_numb=input()
    zz.append(phone_numb)
   
for i in range (len(zz)):
    sharma.append((zz[atit][0]))

    atit+=1

gopal=["7","8","9"]
ramsharan=0
print(sharma)
for i in range (a):
    if sharma[0+ramsharan] in gopal:
            print("YES")
    else:
            print("NO")

    ramsharan+=1
    


    
