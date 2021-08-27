class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def check(self):
        for i in range(0, len(self.items)):
            for n in range(0, len(self.items)):
                while i < n:
                    if self.items[i] == "(" or self.items[i] == "{" or self.items[i] == "[":
                        print("getting in second if")
                        if self.items[n] == ")" or self.items[n] == "}" or self.items[n] == "]":
                            print("success")
                            return True
                        else:
                            print("fail")
                            return False
                    else:
                        print("udd gaya")
                        return False

        # return False
