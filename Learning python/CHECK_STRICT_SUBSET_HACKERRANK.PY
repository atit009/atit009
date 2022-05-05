
def checker(A,total_sets):
    z=[]
    if(all(x in A for x in total_sets)):
        z.append(True)
    else:
        z.append(False)

    

    j=all(z)
    return(j)

if __name__=="__main__":
    total_sets=[]
    hari=[]
    A=list(map(int,input().split()))
    No_of_sets=int(input())
    for i in range (No_of_sets):
        setss=list(map(int,input().split()))
        total_sets.append(setss)
    count=0
    for i in range (No_of_sets):
        xyz=(checker(A,total_sets[count]))
        count+=1
        hari.append(xyz)
# print(hari)
atit=all(hari)
print(atit)