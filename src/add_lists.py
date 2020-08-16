ns = [1,2,3]
ms = [4,5,6]

# same as len
def length(ns):
    count = 0
    for i in ns:
        count = count + 1
    return count

print(ns + ms)        

sum = [ns[i] + ms[i] for i in range(lengh(ns))]

print(sum)