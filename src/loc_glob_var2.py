n=1

def f():
    global n
    n=2
    print(n)

print(n)
f()
print(n)