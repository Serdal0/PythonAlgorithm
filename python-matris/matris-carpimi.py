"İki matrisin çarpımını hesaplayan prog?"

m=[[5,4],[2,3],[3,1]]
n=[[2,7,6],[1,1,2]]
k=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m)):
    for j in range(len(m)):
        k[i][j]=m[i][0]*n[0][j]+m[i][1]*n[1][j]

print(k)