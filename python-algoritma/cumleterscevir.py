"Girilen cümleyi tersten yazdırın?"
isim = input("İsminizi giriniz: ")
print(isim[::-1])




isim = str(input("İsminizi giriniz: "))
uzunluk = len(isim)
ters = ""
for i in range(uzunluk-1,-1,-1):
    ters +=isim[i]
print(ters)