"""
Elements of Programming Interviews: 10.2

given an array that has elements in increasing order, then decreasing order, then increasing again, etc.. return
the fully sorted array

we know that the list starts out increasing, so we will start at the second element.
every step of the iteration, we have to check the previous item to determine if we are switching directions.
if we are switching directions, slice off the appropriate section (keep in mind the decreasing section needs to be reversed)
and add it to the sorted lists.  update starting position to this new element and switch the current direction.
when finished, we can merge these sorted arrays together.
"""

from heapq import merge

INCREASING = 0
DECREASING = 1

def sort_increasing_decreasing_array(lst):
    sorted_lists = []
    start = 0
    current_direction = INCREASING

    for i in range(1, len(lst) + 1):
        if (i == len(lst) or
            lst[i - 1] >= lst[i] and current_direction == INCREASING or
                lst[i - 1] < lst[i] and current_direction == DECREASING):
                if current_direction == INCREASING:
                    grouping = lst[start:i]
                else:
                    grouping = lst[i-1:start-1:-1]
                sorted_lists.append(grouping)
                start = i
                current_direction = DECREASING if current_direction == INCREASING else INCREASING 

    return merge(sorted_lists) 

sort_increasing_decreasing_array([1,3,4,10,8,7,15,17,9,6,1])
