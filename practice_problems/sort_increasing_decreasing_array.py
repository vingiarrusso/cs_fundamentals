from merge_sorted_arrays import merge_sorted_arrays

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

    return merge_sorted_arrays(sorted_lists)

sort_increasing_decreasing_array([1,3,4,10,8,7,15,17,9,6,1])
