class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, data, node=None):
        if self.root is None:
            self.root = Node(data)
        else:
            if node is None:
                node = self.root
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.create(data, node.left)

            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.create(data, node.right)


def height(node):
    if node.left:
        leftHeight = height(node.left)
    else:
        leftHeight = -1

    if node.right:
        rightHeight = height(node.right)
    else:
        rightHeight = -1

    return 1+max(leftHeight, rightHeight)


print(" *** Binary Search Tree Height ***")

tree = BinarySearchTree()

arr = list(map(int, input("Enter Input : ").split()))

for e in arr:

    tree.create(e)


print("Height = ", height(tree.root), end="\n\n")
