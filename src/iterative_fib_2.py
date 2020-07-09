n = 20

fib_one = 0
fib_two = 1
if n == 0:
    fib = fib_one
elif n == 1:
    fib = fib_two
else:
    for i in range(2,n+1):
        fib = fib_one + fib_two
        fib_one = fib_two
        fib_two = fib
print(fib)