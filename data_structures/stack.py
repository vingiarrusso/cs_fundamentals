"""
Stack class using singly linked list
"""

class DataNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, node):
        node.next = self.top
        self.top = node

    def pop(self):
        old_top = self.top
        self.top = self.top.next
        return old_top

    def peek(self):
        return self.top


s = Stack()
s.push(DataNode(1))
assert s.top.data == 1
s.push(DataNode(2))
n = s.pop() 
assert n.data == 2
p = s.peek()
assert p.data == 1

