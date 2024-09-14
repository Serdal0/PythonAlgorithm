def fak(x):

    carpım=1
    for i in range(1,x+1):
        carpım*=i
    return carpım

n=int(input("Kaç satır?: "))
n-=1
for i in range(n+1):
    for j in range(n,-1,-1):
        print(" ",end="")
    for j in range(i+1):

        c=fak(i)/(fak(i-j)*fak(j))
        print(int(c),end=" ")
    n-=1
    print()