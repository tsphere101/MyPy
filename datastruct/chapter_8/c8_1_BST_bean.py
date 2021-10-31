
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print("*")

        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if data == node.data:
            return node

        elif data < node.data:
            print("L",end = '')
            if node.left:
                node.left = self._insert(data, node.left)
                return node
            else:
                node.left = Node(data)
                print("*")
                return node

        elif data > node.data:
            print("R",end = '')
            if node.right:
                node.right = self._insert(data, node.right)
                return node
            else:
                node.right = Node(data)
                print("*")
                return node

        return node


if __name__ == "__main__":

    t = BST()

    inp = input("Enter Input : ").split()

    for data in inp :
        t.insert(int(data))

    

