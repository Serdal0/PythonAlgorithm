"Girilen sayının Jumbled (komşu rakamlar arasındaki fark maksimum 1) olup olmadığını bulunuz? "


n = int(input("Sayı giriniz: "))

c = 0
x = n%10
while n>10:
    son = n%10
    if abs(son-x)>=1:
        c=1
        break
    x=son
    n=n//10

if c==0:
    print("Başarılı")
else:
    print("hata")
