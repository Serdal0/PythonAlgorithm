"Girilen bir sayının asal olup olmadığını bulunuz?"

n = int(input("Asal sayı olup olmadığını öğrenmek istediğiniz sayıyı giriniz: "))

if n>1:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} sayısı asal değildir.")
            break
    else:
        print(f"{n} sayısı asaldır.")
else:
    print("Sayı asal değildir")
