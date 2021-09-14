class BinarySearchNode:
    def __init__(self, data=None):
        self.data = [data]
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data[0]:
            self.data.append(data)

        elif data < self.data[0]:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchNode(data)

        elif data > self.data[0]:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)

    def in_order_traversal(self):
        elements = []

        # visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()

        elements += self.data

        # visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements += self.data
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements += self.data

        return elements

    def search(self, data):
        if data == self.data[0]:
            return True

        elif data < self.data[0]:
            # data might be in the left child
            if self.left:
                return self.left.search(data)
            else:
                return False

        elif data > self.data[0]:
            # data might be in the right child
            if self.right:
                return self.right.search(data)
            else:
                return False


class BinarySearchTree:

    def __init__(self, iterable=None):

        self.size = 0
        self.root = None

        if iterable is not None:
            for data in iterable:
                self.append(data)

    def append(self, data):
        if self.root is None:
            self.root = BinarySearchNode(data)
        else:
            self.root.add_child(data)

    def find_min(self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.data[0]

    def find_max(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.data[0]

    def calculate_sum(self):
        elements = self.root.in_order_traversal()
        result = elements[0]
        for i in range(1, len(elements)):
            result += elements[i]
        return result

    def __str__(self):
        elements = self.root.in_order_traversal()
        return "[" + ",".join(str(x) for x in elements) + "]"

    def __contains__(self, data):
        return self.root.search(data)


def BinarySort(iterable):

    class Node:
        def __init__(self, data):
            self.data = [data]
            self.left = None
            self.right = None

        def add_child(self, data):
            if data == self.data[0]:
                self.data.append(data)
            elif data < self.data[0]:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = Node(data)
            elif data > self.data[0]:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = Node(data)

        def in_order_traversal(self):
            elements = []

            if self.left:
                elements += self.left.in_order_traversal()

            elements += self.data

            if self.right:
                elements += self.right.in_order_traversal()

            return elements

    root = Node(iterable[0])
    for i in range(1, len(iterable)):
        root.add_child(iterable[i])

    elements = root.in_order_traversal()
    return elements


if __name__ == "__main__":
    elements = [5, 2, 3, 6, 6, 6, 6, 6, 8, 1, 13, 29, 59, 32, 37, 15]
    a = BinarySearchTree(elements)