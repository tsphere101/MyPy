
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if data < self.data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return self.left
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return self.left

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            self.root.insert(data)
            return self.root

    def find_max(self):
        if self.root:
            return self.root.find_max()
        else:
            return None

    def find_min(self):
        if self.root:
            return self.root.find_min()
        else:
            return None

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def __str__(self):
        if self.root != None:
            level = 0
            self.printTree(self.root.right, self.root + 1)
            print('     ' * level, self.root)
            self.printTree(self.root.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)

print("--------------------------------------------------")
print("Min :",T.find_min())
print("Max :",T.find_max())
