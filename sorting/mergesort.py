def mergesort(lst):
    if len(lst) < 2:
        return lst

    middle = len(lst) // 2
    return merge(mergesort(lst[0:middle]), mergesort(lst[middle:]))

def merge(lst1, lst2):
    merged = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
   

    while i < len(lst1):
        merged.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged.append(lst2[j])
        j += 1
   
    return merged


mergesort([1,8,3,47,3,9,8,4,7,2,1,4,55,33,22,48,74])
