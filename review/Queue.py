class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self, val):
        self.front = Node(val, self.front)

    def pop(self):
        if self.front is None:
            return None
        node = self.front
        self.front = self.front.next
        return node.next

    def is_empty(self):
        return self.front is None