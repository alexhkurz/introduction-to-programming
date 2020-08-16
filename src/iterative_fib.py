n = 100000

def fib(n):
    fib_one = 0
    fib_two = 1
    for i in range(0,n+1):
        if i == 0:
            fib = fib_one
        elif i == 1:
            fib = fib_two
        else:
            fib = fib_one + fib_two
            fib_one = fib_two
            fib_two = fib
    return fib        

print(fib(n))
