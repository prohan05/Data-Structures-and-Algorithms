class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.left = tea
leftChild.right = coffee
newBT.left = leftChild
newBT.right = rightChild


def levelOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
        return "Not Found"


# print(searchBT(newBT, "Tea"))
# Insert Method
def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            else:
                root.value.left = newNode
                return "Successfully nserted"
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
            else:
                root.value.right = newNode
                return "Successfully Inserted"

# newNode = TreeNode("Cola")
# print(insertBT(newBT, newNode))
# levelOrderTrav(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
        deepestNode = root.value
        return deepestNode


# deepestNode = getDeepestNode(newBT)
# print(deepestNode.data)

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.right:
                if root.value.right is dNode:
                    root.value.right = None
                    return
                else:
                    customQueue.enqueue(root.value.right)
            if root.value.left:
                if root.value.left is dNode:
                    root.value.left = None
                    return
                else:
                    customQueue.enqueue(root.value.left)


# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
# levelOrderTrav(newBT)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "BT not present"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Successfully deleted"
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
        return "Failed to delete"


# print(deleteNodeBT(newBT, 'Hot'))
# levelOrderTrav(newBT)
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "BT deleted"


print(deleteBT(newBT))
levelOrderTrav(newBT)
