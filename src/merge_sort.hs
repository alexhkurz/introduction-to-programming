my_list = [4,3,2,1]

merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys) = if x <= y then x:merge xs (y:ys) else y:merge (x:xs) ys

merge_lists [] = []
merge_lists [l] = [l]
merge_lists [l1,l2] = [merge l1 l2]
merge_lists (l1:l2:ls) = merge_lists ((merge l1 l2) : (merge_lists ls))

sort l = merge_lists [[x] |  x <- l] 


