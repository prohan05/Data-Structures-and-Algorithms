class SLLnode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLnode object: data = {}".format(self.data)

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object: head = {}".format(self.head)

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = SLLnode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_front(self, new_data):
        # Adds a node whose data is new_data argument to the front of the linked list
        temp = SLLnode(new_data)
        temp.set_next(self.head)
        self.head = temp

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

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

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

    def remove(self, data):
        # Time Complexity is O(n)
        # for empty list
        if self.head is None:
            return "bruh its already empty"
        # when non empty
        current = self.head
        prev = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "node like that doesn't exist"
                else:
                    prev = current
                    current = current.get_next()
        if prev is None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())

    def delete_at_pos(self, position):
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        count = 1
        while current_node and count != position:
            prev = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("not present")
            return
        new_node = SLLnode(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def node_swap(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next
        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key1:
            prev2 = curr2
            curr2 = curr2.next
        if not curr1 or not curr2:
            return
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1
        curr1.next, curr2.next = curr2.next, curr1.next

    # Iterative
    def rev_ll(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = cur.next
            cur = nxt
        self.head = prev

    # Recursive
    def rev_ll_rec(self):
        def rev_ll_recc(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return rev_ll_recc(cur, prev)

        self.head = rev_ll_recc(cur=self.head, prev=None)

    # Merging 2 sorted linked test
    # Append bot the lists
    # list1.merge_sorted(list2)
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
            while p and q:
                if p.data <= q.data:
                    s.next = p
                    s = p
                    p = s.next
                else:
                    s.next = q
                    s = q
                    q = s.next
            if not p:
                s.next = q
            if not q:
                s.next = p
            return new_head

    # Removing duplicates
    def remove_dupli(self):
        cur = self.head
        prev = None
        dupli_val = dict()
        while cur:
            if cur.data in dupli_val:
                # Remove Node
                prev.next = cur.next
                cur = None
            else:
                dupli_val[cur.data] = 1
                prev = cur
            cur = prev.next

# Printing Nth to Last Node - Method 1
    def nth2last(self, n):
        list_length = self.size()
        cur = self.head
        while cur:
            if list_length == n:
                print(cur.data)
                return cur
            list_length -= 1
            cur = cur.next
        if cur is None:
            return

# Printing Nth to Last Node - Method 2
    def n2last(self, n):
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + 'is greater than the number of nodes in list')
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data

# Occurrence counting
# Iterative Method
    def count_occurences_itr(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

# Recursive Method
    def count_occurences_rec(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_rec(node.next, data)
        else:
            return self.count_occurences_rec(node.next, data)

# Rotate List
    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        q.next = self.head
        self.head = p.next
        p.next = None

# Palindrome in linked list
# method 1
    def is_palindrome(self):
        s = ''
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

# Method 2
    def palindrome(self):
        p = self.head
        q = self.head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i -1]
        count = 1
        while count < i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return False

# Tail node to head
    def move_tail2head(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

# Sum of 2 lists, 365 + 248
# 3 6 5
# 2 4 8
# -----
# 6 1 3
    def sum2lists(self, llist):
        p = self.head
        q = llist.head
        sum_list = SLL()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                i = 0
            else:
                i = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print_list()

sll = SLL()
sll.add_front(10)
sll.add_front(20)
sll.add_front(30)
sll.add_front(40)
sll.add_front(50)
"""
print("Item Count: ", sll.size())
print("Find 20: ", sll.search(20))
print("find 90: ", sll.search(90))
"""
sll.remove(40)
print(sll.size())
print("find number at position 4: ", sll.search(sll.head))