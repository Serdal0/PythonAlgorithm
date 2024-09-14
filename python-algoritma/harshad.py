"N’e kadar ki Harshad (sayının kendisi rakamları toplamına bölünüyor) olanları listele? "

n = int(input("Sayı gir: "))

numbers=[]
for i in range(1,n+1):
    hs=i
    toplam=0
    while i>0:
        x = i%10
        toplam +=x
        i = i//10
        if i==0:

            if hs%toplam==0:
                numbers.append(hs)
print(numbers)