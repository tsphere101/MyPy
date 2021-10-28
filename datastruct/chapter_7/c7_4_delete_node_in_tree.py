class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    # def insert(self, data):
    #     if data < self.data:
    #         if self.left is not None:
    #             return self.left.insert(data)
    #         else:
    #             self.left = Node(data)
    #             return self.left
    #     else:
    #         if self.right is not None:
    #             return self.right.insert(data)
    #         else:
    #             self.right = Node(data)
    #             return self.left

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

    def find_max(self, node=None):
        if self.root is None:
            return None

        if node is None:
            node = self.root

        if node.right:
            return self.find_max(node.right)
        else:
            return node

    def find_min(self, node=None):
        if self.root is None:
            return None

        if node is None:
            node = self.root

        if node.left:
            return self.find_min(node.left)
        else:
            return node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def count_if_less_than_or_eq(self, node, data):
        if self.root:

            if node is None:
                return 0

            if node.data <= data:
                count = 1 + \
                    self.count_if_less_than_or_eq(
                        node.left, data) + self.count_if_less_than_or_eq(node.right, data)

            else:
                count = self.count_if_less_than_or_eq(node.left, data)

            return count

        else:
            return 0

    def search(self, data, node=None):

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

    def in_order_successor(self, node):
        if self.root is None:
            return None

        if node.right:
            # case I : has right node
            p = node.right
            while (p.left):
                p = p.left
            return p

        else:
            # case II : has no right node
            succ = None
            p = self.root
            while(p is not None):
                if node.data > p.data:
                    p = p.right
                if node.data < p.data:
                    succ = p
                    p = p.left
                else:
                    break

            return succ

    def delete(self, data):

        self.root = self._delete_node(self.root, data)

    def _delete_node(self, node, data):
        if self.root is None:
            raise ValueError(f"delete from empty tree")

        if node is None:
            raise ValueError(f"{data} is not contained in the tree")

        # Do a search
        if data == node.data:
            # 4 cases
            if not node.left and not node.right:
                # no child
                # if node == self.root: self.root = None
                return None
            elif node.left and not node.right:
                # has only left child
                # if node == self.root: self.root = node.left
                return node.left
            elif not node.left and node.right:
                # has only right child
                return node.right
            else:
                # has both children

                succ = self.in_order_successor(node)

                node.data = succ.data

                node.right = self._delete_node(node.right, succ.data)

        elif data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)

        return node

    def in_order_traversal(self, node=None):
        if self.root is None:
            return None
        if node is None:
            node = self.root
        elements = []

        if node.left:
            elements += self.in_order_traversal(node.left)

        elements.append(node.data)

        if node.right:
            elements += self.in_order_traversal(node.right)

        return elements

    def is_empty(self):
        return self.root is None

    def __str__(self):
        if self.root != None:
            level = 0
            self.printTree(self.root.right, self.root + 1)
            print('     ' * level, self.root)
            self.printTree(self.root.left, level + 1)
        return None


if __name__ == "__main__":

    # t = BST()
    # t.insert(3)
    # t.insert(2)
    # t.insert(1)
    # t.insert(12)
    # t.printTree(t.root)

    inp = input("Enter Input : ").split(',')
    t = BST()
    for data in inp:
        spl = data.split()
        command = spl[0]
        value = int(spl[1])

        if command.lower() == 'i':
            print(f"insert {value}")
            t.insert(value)
            t.printTree(t.root)

        elif command.lower() == 'd':
            print(f"delete {value}")
            try:
                t.delete(value)
            except:
                print("Error! Not Found DATA")
            t.printTree(t.root)
