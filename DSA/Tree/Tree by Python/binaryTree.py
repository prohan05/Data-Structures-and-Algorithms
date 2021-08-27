class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "inserted"

    def searchinBT(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Failure"

    # Pre-order Traversal
    def preOrderTrav(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTrav(index*2)
        self.preOrderTrav(index*2 + 1)

    # In-Order Traversal
    def inOrderTrav(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTrav(index*2)
        print(self.customList[index])
        self.inOrderTrav(index*2 + 1)

    # Post-Order Traversal
    def postOrderTrav(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTrav(index*2)
        self.postOrderTrav(index*2 +1)
        print(self.customList[index])

    # Lever-order Traversal
    def levelOrderTrav(self, index):
        for i in range(index, self.lastUsedIndex):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "It's empty"
        for i in range(1, self.lastUsedIndex +1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "deleted"


newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.insertNode("Cola")
#newBT.preOrderTrav(1)
# newBT.inOrderTrav(1)
# newBT.postOrderTrav(1)
print(newBT.deleteNode("Hot"))
newBT.levelOrderTrav(1)



