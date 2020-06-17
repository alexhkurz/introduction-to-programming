n = 30
count = 0

def fib(n):
    global count
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        count = count + 2
        return fib(n-1)+fib(n-2)

print("fib(n):",fib(n))
print("count:", count)