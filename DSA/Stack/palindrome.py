class Palindrome:

    def __init__(self):
        self.item = []

    def add_front(self, item):  #  runtime O(n)
        return self.item.insert(0, item)

    def add_rear(self, item):  #  runtime O(1)
        return self.item.append(item)

    def remove_front(self):  #  runtime O(n)
        return self.item.pop(0)

    def remove_rear(self): #runtime O(1)
        return self.item.pop()

    def size(self):
        return len(self.item)


def matching(string):
    word = Palindrome()
    for element in string:
        word.add_rear(element)

    while word.size() >= 2:
        first = word.remove_front()
        last = word.remove_rear()
        if first != last:
            print("not a palindrome")

    print('is a palindrome')


print(matching('level'))
print(matching('duuh'))

