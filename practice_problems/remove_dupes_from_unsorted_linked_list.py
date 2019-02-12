import sys
sys.path.insert(0, '../data_structures')

from linked_list_node import ListNode
from singly_linked_list import LinkedList

def remove_dupes(ll):
    s = set()
    n = ll.head

    while n:
        s.add(n.data)
        if n.next:
            if n.next.data in s:
                n.next = n.next.next
        n = n.next   
    
    return ll

ll = LinkedList()
ll.append_to_list(ListNode(1))
ll.append_to_list(ListNode(2))
ll.append_to_list(ListNode(3))
ll.append_to_list(ListNode(4))
ll.append_to_list(ListNode(4))
ll.append_to_list(ListNode(5))
remove_dupes(ll)
ll._print_list()

