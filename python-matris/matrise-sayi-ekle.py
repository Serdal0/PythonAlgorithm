"Verilen sayıyı matrisin k. indeksine yerleştir?"

m=[[7,6,42],
[4,23,5],
[13,12,9]]

while True:
    satir=int(input("Kaçıncı satır: "))
    sutun=int(input("Kaçıncı sutun: "))
    k=int(input("Yeni sayı: "))
    if 0<satir<=3 and 0<sutun<=3:

        for i in range(len(m)):
            for j in range(len(m)):
                if m[i][j]==m[satir-1][sutun-1]:
                    m[i][j]=k
        print(m)
        break
    else:
        print("Lütfen satır ve sutun sayısını [1,3] aralığında giriniz: ")
    