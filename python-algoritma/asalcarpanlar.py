"Girilen bir sayının asal çarpanlarını bulan program?"

n = int(input("sayı gir: "))

bolen = 2
c =0
for i in range(1,n+1):
    
    if n%bolen==0:
        n/=bolen
        c+=1
        if c==1:
            print(bolen)
    else:
        bolen +=1
        c=0