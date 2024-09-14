"Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz?" 

n = int(input("Pronic sayı olup olmadığını öğrenmek istediğiniz sayıyı giriniz: "))
a = 1
b = a+1

while a<n:
    a+=1
    if b*a==n:
        print("Başarılı")
        break
else:
    print("hata")