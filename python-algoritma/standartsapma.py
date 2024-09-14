"Girilen 5 sayının standart sapmasını bulan program?"

liste=[]
top=0

for i in range(5):
    n = int(input("Sayı gir:"))
    liste.append(n)
    top+=n
o=top/5
top2=0
for i in range(5):
    top2+=(liste[i]-o)**2
ss=(top2/4)**0.5
print("Standart sapma değeri: {}".format(ss))