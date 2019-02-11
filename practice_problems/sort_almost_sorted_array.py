"""
Elements of Programming Interviews: 10.3

given a nearly sorted array and at most how far away a number is from its final position (k), 
return the sorted list of numbers

make a min heap of the first k numbers
iterate through the rest of the list, when the heap length is greater than k, pop the min
and append to the result.
pop the remaining heap members to the result and return it
"""

from heapq import heappush, heappop

def sort_almost_sorted_array(lst, k):
    result = []

    if not lst:
        return result 
    
    min_heap = []

    for i in range(k):
        heappush(min_heap, lst[i])
        
    for i in range(k, len(lst)):
        heappush(min_heap, lst[i])

        if len(min_heap) > k:
            result.append(heappop(min_heap))

    while len(min_heap):
        result.append(heappop(min_heap))

    return result

sort_almost_sorted_array([4,9,1,8,14,15,10,12,13], 3)
