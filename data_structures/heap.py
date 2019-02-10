def heapify(lst):
    heap = []
    for i in range(len(lst)):
        heap_push(heap, lst[i])
    return heap

def heap_push(heap, item):
    heap.append(item)
    bubble_up(heap, len(heap))

def find_parent(idx):
    return -1 if int(idx) == 0 else int(idx) // 2

def bubble_up(heap, idx):
    if find_parent(idx) == -1:
       return

    if heap[find_parent(idx)] > heap[idx]:
        swap(heap, find_parent(idx), idx)
        bubble_up(heap, find_parent(idx))

def swap(heap, a, b):
    heap[a], heap[b] = heap[b], heap[a]
