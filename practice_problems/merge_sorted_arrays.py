"""
make a min heap out of the first elements of each list
pop the smallest element off the heap, append to result
add the next element in the list this element came from to the heap
continue until there are no more elements in the heap
"""

import heapq

def merge_sorted_arrays(array_list):
    min_heap = []
    result = []
    array_iterables = [iter(lst) for lst in array_list]

    for i, iterable in enumerate(array_iterables):
        item = next(iterable, None)
        if item is not None:
            heapq.heappush(min_heap, (item, i))
    
    while min_heap:
        smallest_item, iterable_idx_smallest_came_from = heapq.heappop(min_heap)
        result.append(smallest_item)
        next_smallest_item = next(array_iterables[iterable_idx_smallest_came_from], None)
        
        if next_smallest_item is not None:
            heapq.heappush(min_heap, (next_smallest_item, iterable_idx_smallest_came_from))

    return result


merge_sorted_arrays([[1,3,5,73,103,107], [2,8,10,15,29,40,194,208], [3,52,84,193,987,1003]])


