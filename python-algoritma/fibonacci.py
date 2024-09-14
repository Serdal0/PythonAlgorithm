"Fibonacci====================="

n = int(input("n sayısı gir: "))

a = 0
b = 1
fib = 0
print(a)
print(b)

for i in range(1,n-1):
    fib=a+b
    print(fib)
    a=b
    b=fib