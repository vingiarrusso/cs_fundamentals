"""
Queue class using singly linked list
"""

class DataNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.end = None
    
    def enqueue(self, node):
        if self.front is None:
            self.front = node

        if self.end is not None:
            self.end.next = node
        
        self.end = node
        

    def dequeue(self):
        if not self.front:
            raise Exception('Cannot dequeue an empty queue')

        old_front = self.front

        if self.front is not None:
            self.front = self.front.next
        
        return old_front

    def peek(self):
        return self.front
    
    def isEmpty(self):
        return self.front == None

q = Queue()
q.enqueue(DataNode(1))
assert q.peek().data == 1
q.enqueue(DataNode(2))
q.enqueue(DataNode(3))
assert q.dequeue().data == 1
assert q.peek().data == 2
assert not q.isEmpty()
q.dequeue()
q.dequeue()
assert q.isEmpty()
