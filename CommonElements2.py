def thor(list1 , list2):
    return list(set(list1) & set(list2))

list1 = [1 , 2 , 3, 4]
list2 = [3 , 4 , 5 , 6]
result = thor(list1 , list2)
print(result)