
"PASCAL üçgeninin n. satırını üretiniz?"

def fak(x):

    carpım=1
    for i in range(1,x+1):
        carpım*=i
    return carpım

n=int(input("Kaçıncı satır?: "))
n-=1
for i in range(n+1):

    c=fak(n)/(fak(n-i)*fak(i))
    print(c,end=" ",)