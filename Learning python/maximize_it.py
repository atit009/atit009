a=list(map(int,input().split()))

new_list=[]
for i in range (a[0]):
    list_of_all=list(map(int,input().split()))
    new_list.append(list_of_all)


print(new_list)


for i in new_list:
    for j in i:
        a