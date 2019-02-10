def heapify(lst):
    heap = []
    for i in range(len(lst)):
        heap_push(heap, lst[i])
    return heap

def heap_push(heap, item):
    l = len(heap)
    heap.append(item)
    bubble_up(heap, l)

def bubble_up(heap, idx):
    if find_parent(idx) == -1:
       return

    if heap[find_parent(idx)] > heap[idx]:
        swap(heap, find_parent(idx), idx)
        bubble_up(heap, find_parent(idx))

def find_parent(idx):
    return -1 if int(idx) == 0 else int(idx) // 2

def swap(heap, a, b):
    heap[a], heap[b] = heap[b], heap[a]

def heap_pop_min(heap):
    if not len(heap):
        raise Exception('Cannot pop min of empty heap')
    
    minimum = heap[0]
    heap[0] = heap.pop()
    bubble_down(heap, 0)

    return minimum

def bubble_down(heap, idx):
    child = find_young_child(idx)
    min_idx = idx

    for i in range(2): # 2 children to compare with (2n and 2n + 1)
        if (i + child) < len(heap):
            if heap[min_idx] > heap[i + child]:
                min_idx = i + child

    if min_idx != idx:
        swap(heap, idx, min_idx)
        bubble_down(heap, min_idx) 

def find_young_child(idx):
    return 2*idx
