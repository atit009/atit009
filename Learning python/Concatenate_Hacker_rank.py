import numpy as np
a=list(map(int,input().split()))

new_list=[]
for i in range (a[0]+a[1]):
    lis1=list(map(int,input().split()))
    new_list.append(lis1)

final_answer=np.array(new_list)
print(final_answer)