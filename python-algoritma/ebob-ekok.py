
"Girilen iki sayının OKEK (ortak katların en küçüğü) hesaplayan program?"

"Girilen iki sayının OBEB (ortak bölenlerin en büyüğü) hesaplayan program?"


sayi1 = int(input("Birinci Sayıyı Giriniz : "))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))
if (sayi1>sayi2):
    kucuksayi = sayi2
else:
    kucuksayi = sayi1
for i in range(1,kucuksayi+1):
    if (sayi1 % i==0) and (sayi2%i ==0):
        ebob = i

ekok = (sayi1*sayi2)//ebob
print(f"Ebob = {ebob}")
print(f"Ekok = {ekok}")