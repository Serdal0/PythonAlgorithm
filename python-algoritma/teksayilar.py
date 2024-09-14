"N’e kadar tek sayıları yazdıran program?"

n = int(input("n: "))

x = 0
while x<=n:
    if x%2==1:
        print(x)
    x+=1

n = int(input("n: "))

for i in range(n):
    if i%2==1:
        print(i)
    i+=1