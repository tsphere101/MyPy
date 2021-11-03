class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:

    # Preorder
    # PostOrder
    # Inorder
    # Level Order

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                node.left = self._insert(data, node.left)
                return node
            else:
                node.left = Node(data)
                return node
        elif data > node.data:
            if node.right:
                node.right = self._insert(data, node.right)
                return node
            else:
                node.right = Node(data)
                return node

        else:
            # print("CASE OF EQUAL")
            if node.right:
                node.right = self._insert(data,node.right)
            return node

    def printBST(self, node, level=0):
        if node != None:
            self.printBST(node.right, level + 1)
            print('     ' * level, node.data)
            self.printBST(node.left, level + 1)

    def pre_order_traversal(self, node=None):
        if self.root is None:
            return

        if node is None:
            node = self.root

        print(node.data, end=" ")

        if node.left:
            self.pre_order_traversal(node.left)

        if node.right:
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node=None):
        if self.root is None:
            return

        if node is None:
            node = self.root

        if node.left:
            self.in_order_traversal(node.left)

        print(node.data, end=" ")

        if node.right:
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node=None):
        if self.root is None:
            return

        if node is None:
            node = self.root

        if node.left:
            self.post_order_traversal(node.left)


        if node.right:
            self.post_order_traversal(node.right)

        print(node.data, end=" ")

    def level_order_traversal(self,node = None):
        if self.root is None:
            return

        if node is None:
            node = self.root

        queue = []        
        queue.append(node)

        while len(queue) != 0:
            n = queue.pop(0)

            if n.left:
                queue.append(n.left)
            
            if n.right:
                queue.append(n.right)

            print(n.data,end = " ")


if __name__ == "__main__":

    print(" *** Binary Search Tree ***")
    inp = input("Enter Input : ")
    data = [int(x) for x in inp.split()]

    t = BST()
    for d in data:
        t.insert(d)

    print()

    print(" --- Tree traversal ---")
    print("Level order : ", end="")
    t.level_order_traversal()
    print()
    print("Preorder : ", end="")
    t.pre_order_traversal()
    print()
    print("Inorder : ", end="")
    t.in_order_traversal()
    print()
    print("Postorder : ", end="")
    t.post_order_traversal()