# https://docs.python.org/3/tutorial/introduction.html#lists
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/library/functions.html#id
# https://stackoverflow.com/questions/725782/in-python-what-is-the-difference-between-append-and/725882
# https://stackoverflow.com/questions/3917574/how-is-pythons-list-implemented

from termcolor import colored

my_number = 0
my_list = [0]

def plus_one_number(n):
    n = n+1
    return n

def plus_one_list(l):
    l = l+[1]
    return l

def plus_one_list_2(l):
    l += [1]
    return l

def append_one(l):
    l.append(1)

print()

print(my_number, 'is my_number')
print(plus_one_number(my_number), 'is the result of', colored('plus_one_number(my_number)','red'))
print(my_number, 'is my_number')

print()

print(my_list, 'is my_list')
print(plus_one_list(my_list), 'is the result of', colored('plus_one_list(my_list)','red'))
print(my_list, 'is my_list')

print()

print(my_list, 'is my_list')
print(plus_one_list_2(my_list), 'is the result of', colored('plus_one_list_2(my_list)','red'))
print(my_list, 'is my_list')

print()

print(my_list, 'is my_list')
print(append_one(my_list), 'is the result of', colored('append_one(my_list)','red'))
print(my_list, 'is my_list')

print()

