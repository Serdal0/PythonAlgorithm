"Girilen sayının tam bölenlerini bulan program?"

sayi = int(input("hangi sayının bölenlerini bulalım? : "))
 
for i in range(1,sayi):
    if sayi % i == 0:
        print(i)