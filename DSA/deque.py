class Deque:

    def __init__(self):
        self.item = []

    def add_front(self, item):
        #  runtime O(n)
        return self.item.insert(0, item)

    def add_rear(self, item):
        #  runtime O(1)
        return self.item.append(item)

    def remove_front(self):
        #  runtime O(n)
        if self.item:
            return self.item.pop(0)
        return None

    def remove_rear(self):
        #  runtime O(1)
        return self.item.pop()

    def peek_front(self):
        # runtime O(1)
        if self.item:
            return self.item[0]
        return None

    def peek_rear(self):
        # runtime O(1)
        if self.item:
            return self.item[-1]
        return None

    def size(self):
        return len(self.item)

    def is_empty(self):
        return self.item == []


