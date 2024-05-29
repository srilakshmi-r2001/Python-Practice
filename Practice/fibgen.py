def genfib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        temp = a
        a = b
        b = b + temp

fib = genfib(10)

for i in fib:
    print(i)