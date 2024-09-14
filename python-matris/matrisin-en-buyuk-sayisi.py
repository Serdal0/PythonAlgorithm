"Matristeki en büyük sayıyı bul."

m=[[7,6,3],
[4,23,3],
[13,3,9]]

n=[]

for i in range(len(m)):
    for j in range(len(m)):
        n.append(m[i][j])
maks=0
for i in n:
    if maks<i:
        maks=i
print("Matrisin en büyük değeri:",maks)