import random
Alphabet_small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Alphabet_Big=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
KEYS_=["!",'@',"#",'$',"%","^","&","*","(",")","_",'-',"+","="]
z=[]
z.extend(Alphabet_small)
z.extend(Alphabet_Big)
z.extend(KEYS_)
random.shuffle(z)
a=int(input("Enter the length of your Password\n"))
b=z[0:a]

atit=''.join(b)
print(f"Your password is\n{atit}")

# print(z)