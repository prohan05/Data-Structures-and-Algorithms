class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

def rev_str(stack, input_str):
    for letter in input_str:
        stack.push(letter)
    rev_str = ''
    while not stack.is_empty:
        rev_str += stack.pop()

    return rev_str
