import numpy as np
new_list=[]

a=list(map(int,input().split()))
for i in range (a[0]):
    z=list(map(int,input().split()))
    new_list.append(z)


my_array = np.array(new_list )
print (np.transpose(my_array))
print (my_array.flatten())