#!/usr/bin/env python3
y=[]
def mutate_string(string, position, character):
    global y
    for i in string:
        y.append(i)
    y[int(position)]=character
    a=string.replace(y[int(position)],character)
    return a


   

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)