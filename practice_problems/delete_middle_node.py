"""
Cracking the coding interview: 2.3
"""
import sys
sys.path.insert(0, '../data_structures')
from linked_list_node import ListNode
from singly_linked_list import LinkedList

def delete_middle_node(node):
    next_node = node.next.next
    node = node.next 
    node.next = next_node

ll = LinkedList()
node_to_delete = ListNode(4)
ll.append_to_list(ListNode(1))
ll.append_to_list(ListNode(2))
ll.append_to_list(ListNode(3))
ll.append_to_list(node_to_delete)
ll.append_to_list(ListNode(5))
delete_middle_node(node_to_delete)
assert not ll.search(node_to_delete)
