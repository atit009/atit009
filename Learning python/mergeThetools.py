def merge_the_tools(string, k):
    z=[]
    new_list=[]
    new_list2=[]
    zero=0
    count=k
    for i in range (k):  #This is done inorder to put elements accordingly in 3 or 4 or 5 in a group.
        z.append(string[zero:count])
        zero+=k
        count+=k
    for j in range (k):     #    This is done to remove spaces from the list (z)
        for i in z:
            if i=="":
                z.remove(i)

    print(z)
    for i in z:
        for j in i:
            if j not in new_list:
                new_list.append(j)


                    
            


                
    print(new_list)
    print(new_list2)

    
    
    print(string,k)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
            





