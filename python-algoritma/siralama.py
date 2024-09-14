"Elemanları sıralayan program?"

elemansayısı=int(input("Kaç elemanlı bir liste oluşturmak istiyorsunuz?: "))
sayilar=[]

while 1:
        if elemansayısı==0:
                break
        else:
                n= int(input(f"{elemansayısı}. sayıyı giriniz: "))
                sayilar.append(n)
                elemansayısı-=1
        
sayilar.sort(reverse = True)
print(sayilar)
