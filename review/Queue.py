class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None

    def push(self, val):
        if not self.front:
            self.front = Node(val)
            return
        node = self.front
        while node.next:
            node = node.next
        node.next = Node(val)

    def pop(self):
        if self.front is None:
            return None
        node = self.front
        self.front = self.front.next
        return node.val

    def is_empty(self):
        return self.front is None