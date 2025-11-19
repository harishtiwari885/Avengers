
def thor(list1 , list2):
    set2 = set(list2)
    result = []
    for a in list1:
        if a in set2 and a not in result:
            result.append(a)
    return result
list1 = [1 , 2 , 3 , 4]
list2 = [3 , 4 , 5 , 6]
print(thor(list1 , list2))