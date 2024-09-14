"Matrisin transpozunu alın."

m=[[7,6,14,8],
[4,23,5,1],
[13,12,9,2],
[8,9,5,3]
]

for i in range(len(m)):
    for j in range(len(m)):
        m[i][j]=m[j][i]
for k in m:
    for a in k:
        print(a,end=" ")
    print()