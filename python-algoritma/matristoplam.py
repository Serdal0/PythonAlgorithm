"Matrisin satır ve sütun toplamlarını hesapla."

m=[[4,6,3],
[4,2,3],
[8,3,9]]

n=[0,0,0]
k=[0,0,0]


for i in range(len(m)):
    for j in range(len(m)):
        n[j]+=m[i][j]
        k[i]+=m[j][i]
    print(f"{i+1}. satırın toplamı: {n[i]}")
    print(f"{i+1}. sutunun toplamı: {k[i]}")