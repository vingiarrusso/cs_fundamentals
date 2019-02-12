from linked_list_node import ListNode 
import pudb
#pu.db

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append_to_tail(self, node):
        if self.head is None:  # lack of list head means this is the first and only node in the list
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def delete_node(self, node_data):
        if self.head is None:
            raise Exception('cannot delete from empty list')
        
        if self.head.data == node_data:
            self.head = self.head.next 
            if self.head is None:
                self.tail = None # if there's no head, there can be no tail (we deleted the one and only element in the list)
            return self.head

        start = self.head
        while start.next:
            if start.next.data == node_data:
                start.next = start.next.next
                return self.head

            start = start.next

        return self.head 
    
    def _print_list(self):
        # for debugging purposes
        n = self.head
        lst = []
        while n is not None:
            lst.append(n.data)
            n = n.next
        print(lst)
        print('head: {}'.format(None if self.head is None else self.head.data))
        print('tail: {}'.format(None if self.tail is None else self.tail.data))




ll = LinkedList()
ll.append_to_tail(ListNode(1))
assert ll.head.data == 1
assert ll.tail.data == 1
ll.append_to_tail(ListNode(2))
assert ll.head.data == 1
assert ll.tail.data == 2
ll.delete_node(1)
ll._print_list()
ll.delete_node(2)
ll._print_list()
ll.append_to_tail(ListNode(1))
ll.append_to_tail(ListNode(3))
ll.append_to_tail(ListNode(5))
ll.delete_node(3)
ll._print_list()

