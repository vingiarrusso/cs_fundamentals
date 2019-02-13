"""
Cracking the coding interview: 2.2
"""

import sys
sys.path.insert(0, '../data_structures')
from linked_list_node import ListNode
from singly_linked_list import LinkedList

def get_kth_to_last(ll, k):
    slow = ll.head
    dummy = ListNode(None)
    dummy.next = slow
    fast = dummy

    for i in range(k):
        # watch out for k > len of list
        if fast is None:
            return None
        fast = fast.next 

    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow


ll = LinkedList()
ll.append_to_list(ListNode(1))
ll.append_to_list(ListNode(2))
ll.append_to_list(ListNode(3))
ll.append_to_list(ListNode(4))
ll.append_to_list(ListNode(5))
ll.append_to_list(ListNode(6))
get_kth_to_last(ll, 3)

ll.delete_node(6)
ll.delete_node(5)
ll.delete_node(4)
ll.delete_node(3)
ll.delete_node(2)
assert not get_kth_to_last(ll, 3)
