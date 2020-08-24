data Mylist a = 
    Nil |
    Cons a (Mylist a)

len Nil = 0
len (Cons x l) = (len l) + 1
