class Queue:

    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        if self.item:
            return self.item.pop()
        return None

    def peek(self):
        if self.item:
            return self.item[-1]
        return None

    def size(self): #runtime O(1)
        return len(self.item)

    def is_empty(self): # runtime O(1)
        return self.item == []
