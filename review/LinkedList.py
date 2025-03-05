class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.next = None

    def append(self, val):
        if not self.next:
            self.next = LinkedNode(val, None)

        node = self.next
        while node.next:
            self.next = LinkedNode(val, None)

        return node.val