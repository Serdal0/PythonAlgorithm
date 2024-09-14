"Farklı değerlere sahip iki listenin korelasyon katsayısını hesaplayan program?"

x=[]
y=[]
for i in range(5):
    n=int(input("X kümesi eleman: "))
    x.append(n)
    m=int(input("Y kümesi eleman: "))
    
    y.append(m)
    
x = [2,3,1,1,3]
y = [5,5,2,2,1]


x=[]
n = input()
for i in range(5):
    n=int(input("x kümesi için eleman gir: "))
    x.append(n)
y=[]
m = input()
for i in range(5):
    m=int(input("y kümesi için eleman gir: "))
    y.append(m)

xtop=0
ytop=0

xort=0
yort=0


for i in range(5):
    xtop+=x[i]
    ytop+=y[i]
xort=xtop/5
yort=ytop/5


carpim=[]
carp=0
xfark=0
yfark=0
for i in range(5):
    xfark=(x[i]-xort)
    yfark=(y[i]-yort)
    carp=xfark*yfark
    carpim.append(carp)

    
carptopla=0
for i in carpim:
    carptopla+=i

xtop2=0
ytop2=0
for i in range(5):
    xtop2+=(x[i]-xort)**2
    ytop2+=(y[i]-yort)**2

altkısım=(xtop2*ytop2)**0.5

korelasyon=carptopla/altkısım
print(f"Korelasyon değeri: {korelasyon}")