"Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program?"


ilkeleman = int(input("İlk Elemanı giriniz: "))
terimsayisi = int(input("Toplam eleman sayısını giriniz: "))
artismiktari = int(input("Artış Miktarını giriniz: "))

soneleman = (terimsayisi*artismiktari)+ilkeleman

for i in range(ilkeleman,soneleman,artismiktari):
    print(i)