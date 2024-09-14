"Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 0-100 aralığında rastgele bir sayı yerleştiriniz. Daha sonra matrisin iki köşegenin de bulunan sayıların yerlerini aşağıdaki gibi ters çeviren programı yazınız."

import random
n=int(input("Matris boyutunu giriniz: "))

matris=[]
for i in range(n):
    matris2=[]
    for j in range(n):
        a=random.randint(1,100)
        matris2.append(a)
    matris.append(matris2)

for i in matris:
    print(i)
print()

matrisyedek=[]
a=len(matris)-1

for i in range(len(matris)):

    for j in range(len(matris)):
        if i==j:
            matrisyedek.append(matris[i][a])
            matris[i][a]=matris[i][j]
            matris[i][j]=matrisyedek[i]
        
            a-=1

for k in matris:
    print(k)