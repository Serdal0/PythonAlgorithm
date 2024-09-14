"Matris izini (diyagonal toplam) bul."


m=[[7,6,42],
[4,23,5],
[13,12,9]]

x=len(m)-1
top=0
top2=0
for i in range(len(m)):
    for j in range(len(m)):
        if i==j:
            top+=m[i][j]
a=len(m)-1
for i in range(len(m)):
    top2+=m[i][a]
    a-=1
print(f"Sola yatık: {top} \nSağa yatık: {top2}")