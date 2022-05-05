def subset(A,B):
    flag = 0
    if(all(x in B for x in A)):###  Throws true if all elements of B are equals To A
        flag = 1
    if (flag):
        print ("Tes")
    else:
        print ("False")
 
    


if __name__=="__main__":
    a=int(input())
    for i in range (a):
        ex=int(input())
        A=list(map(int,input().split()))
        ex1=int(input())
        B=list(map(int,input().split()))
        (subset(A,B))
