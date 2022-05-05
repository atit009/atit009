from functools import reduce

z=[]
for i in range  (int(input("How many numbers"))):
    inp=int(input("Enter Your number"))
    z.append(inp)

zz=reduce(max,z)
print(zz)
