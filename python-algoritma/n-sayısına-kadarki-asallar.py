"İlk n asal sayısını bulunuz"
def SayiAsalmi(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True

n=int(input("Sayı gir: "))
c=0
sayi=1
while c<n:
    if SayiAsalmi(sayi):
        c+=1
        print(sayi)
    sayi=sayi+1