class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = LinkedNode(val, None)
            return self.head

        node = self.head
        while node.next:
            node.next = LinkedNode(val, None)

        return node