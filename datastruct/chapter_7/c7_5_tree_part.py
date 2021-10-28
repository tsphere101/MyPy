class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, node=None):
        if not self.root:
            self.root = Node(data)
            return

        if node is None:
            node = self.root

        if data < node.data:
            if node.left:
                self.insert(data, node.left)
            else:
                node.left = Node(data)
        elif data > node.data:
            if node.right:
                self.insert(data, node.right)
            else:
                node.right = Node(data)

        return

    def search(self, data, node=None):

        if not self.root:
            raise ValueError(f"{data} is not contained in tree.")

        if node is None:
            node = self.root

        if data == node.data:
            return node
        elif data < node.data:
            if node.left:
                return self.search(data, node.left)
            else:
                raise ValueError(f"{data} is not contained in tree.")
        elif data > node.data:
            if node.right:
                return self.search(data, node.right)
            else:
                raise ValueError(f"{data} is not contained in tree.")

        if self.root:
            if node is None:
                node = self.root

            if data == node.data:
                return node

            if data < node.data:
                return self.search(data, node.left)

            if data > node.data:
                return self.search(data, node.right)

        else:
            return None

    def checkpos(self, data):
        try:
            node = self.search(data)
        except:
            print("Not exist")
            return
        if node is self.root:
            print("Root")

        elif node.left or node.right:
            print("Inner")

        elif not node.left and not node.right:
            print("Leaf")

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


if __name__ == "__main__":
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in range(1, len(inp)):
        root = T.insert(inp[i])
    T.printTree(T.root)
    T.checkpos(inp[0])
