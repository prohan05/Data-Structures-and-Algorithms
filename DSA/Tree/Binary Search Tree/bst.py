class BSTnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insertion
def insertNode(rootNode, node):
    if rootNode.data == None:
        rootNode.data = node
    elif node <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTnode(node)
        else:
            insertNode(rootNode.left, node)
    else:
        if rootNode.right is None:
            rootNode.right = BSTnode(node)
        else:
            insertNode(rootNode.right, node)
    return "Inserted"

# Pre-Order Traversal
def preOrderTrav(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTrav(rootNode.left)
    preOrderTrav(rootNode.right)

# In-Order Traversal
def inOrderTrav(rootNode):
    if not rootNode:
        return
    inOrderTrav(rootNode.left)
    print(rootNode.data)
    inOrderTrav(rootNode.right)


# Post-Order Traversal
def postOrderTrav(rootNode):
    if not rootNode:
        return
    postOrderTrav(rootNode.left)
    postOrderTrav(rootNode.right)
    print(rootNode.data)

"""
# Level-Order Traversal
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
"""


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("Found")
    elif nodeValue < rootNode.data:
        if rootNode.left.data == nodeValue:
            print("Found")
        else:
            searchNode(rootNode.left, nodeValue)
    else:
        if rootNode.right.data == nodeValue:
            print("Found")
        else:
            searchNode(rootNode.right, nodeValue)


def minValue(bstNode):
    current = bstNode
    while current.left is not None:
        current = current.left
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, rootNode)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = minValue(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode


newBST = BSTnode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
# preOrderTrav(newBST)
# inOrderTrav(newBST)
# postOrderTrav(newBST)
# searchNode(newBST, 60)
deleteNode(newBST, 60)

