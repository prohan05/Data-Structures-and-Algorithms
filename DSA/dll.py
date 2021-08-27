class DLLnode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return "DLLnode object: data = {}".format(self.data)

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev


class  DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head = >".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        # time complexity is O(n)
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        # Time Complexity is O(n)
        if self.head is None:
            return 'its empty bruh'

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def add_front(self, new_data):
        # Adds a node whose data is new_data argument to the front of the linked list
        temp = DLLnode(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(temp)
        self.head = temp

    def remove(self, data):
        # Time Complexity is O(n)
        if self.head is None:
            return "its empty, can't remove"

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "Node u need isn't there"
                else:
                    current = current.get_next()

        if current.prev is None:
            self.head = current.get_next()
        else:
            current.prev.set_next(current.get_next())
            current.next.set_prev(current.get_prev())
