mylist = [1,2,3]

def reverse(list):
    newlist = []
    for i in list:
        newlist.insert(0,i)
    return newlist

def reverse2(list):
    newlist = []
    for i in list:
        newlist = [i] + newlist
    return newlist

print (mylist,': mylist')
print (reverse(mylist),': reverse(mylist)')
print (mylist,': mylist')

# it would be interesting to benchmark the two programs 
# and to discuss why one version is faster

