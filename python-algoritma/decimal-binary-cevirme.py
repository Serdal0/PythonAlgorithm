"Girilen onluk sayıyı ikili sayıya dönüştürünüz?"

n=int(input("Sayıyı gir: "))
liste=[]

while n>1:
    mod=n%2
    n=n//2
    liste.append(mod)
    if n==1:
        liste.append(1)
liste = liste[::-1] 

for i in liste:
    print(i, end='')