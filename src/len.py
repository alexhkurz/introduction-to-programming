def length(ns):
    count = 0
    for i in ns:
        count = count + 1
    return count

print("start to compute 1000 x len")

for i in range(1000):
    len(list(range(100000)))

print("computed 1000 x len")
