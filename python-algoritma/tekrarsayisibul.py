def tekrar_sayisi_bul(liste):
    tekrarlar = {}
    

    for eleman in liste:
        if eleman in tekrarlar:
            tekrarlar[eleman] += 1
        else:
            tekrarlar[eleman] = 1
    

    for eleman, tekrar_sayisi in tekrarlar.items():
        print(f"{eleman} elemanı {tekrar_sayisi} kez tekrar ediyor.")

liste = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2]
tekrar_sayisi_bul(liste)