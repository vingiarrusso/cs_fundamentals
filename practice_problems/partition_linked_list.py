"""
Cracking the coding interview: 2.4
"""

import sys
sys.path.insert(0, '../data_structures')
from linked_list_node import ListNode
from singly_linked_list import LinkedList


def partition_linked_list(n, p):
    head = n
    tail = n
    
    while n:
        nxt = n.next
        if n.data < p:
            n.next = head
            head = n
        else:
            tail.next = n
            tail = n
        n = nxt

    tail.next = None
    
    return head

ll = LinkedList()
ll.append_to_list(ListNode(1))
ll.append_to_list(ListNode(4))
ll.append_to_list(ListNode(3))
ll.append_to_list(ListNode(10))
ll.append_to_list(ListNode(8))
ll.append_to_list(ListNode(63))
ll.append_to_list(ListNode(28))
ll.append_to_list(ListNode(13))
new_head = partition_linked_list(ll.head, 28)

result = []
n = new_head
while n:
    result.append(n.data)
    n = n.next
print(result)

