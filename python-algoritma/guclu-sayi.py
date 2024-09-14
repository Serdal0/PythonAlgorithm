"Girilen sayının Güçlü (1! + 4! + 5!  = 1 + 24 + 120 = 145) olup olmadığını bulan program?"


def fak(x):

    carpım=1
    for i in range(1,x+1):
        carpım*=i
    return carpım
toplam=0
n=int(input("Sayı gir:"))
ny=n
while n>0:
    a=n%10
    toplam+=fak(a)
    n//=10

if toplam==ny:
    print(ny," sayısı güçlü sayıdır")
else:
    print(ny,"sayısı güçlü sayı değildir")