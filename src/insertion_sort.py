list = [2,1]

def mysort(list):
    new_list = []           # the sorted list
    for x in list:
        # insert x in new_list
        j = 0               # j is used to computer the index where to insert x
        # compare x against the elements y of new_list
        for y in new_list:
            if x <= y:
                break       # insert x "here", ie at index j
            else:
                j = j + 1   # continue with the next element of new_list
        new_list.insert(j,x)
    return new_list

print(mysort(list))