
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return str(self.data)
        # return "[node:" + str(self.data) + ']'


class AVL:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.length += 1
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                node.left = self._insert(data, node.left)
                return self._rebalance(node)
            else:
                node.left = Node(data)
                self.length += 1
                return node
        elif data > node.data:
            if node.right:
                node.right = self._insert(data, node.right)
                return self._rebalance(node)
            else:
                node.right = Node(data)
                self.length += 1
                return node

    def _rebalance(self, node):
        bf = self.balance_factor(node)

        # Left heavy tree
        if bf > 1:
            if node.left:
                if self.balance_factor(node.left) > 0:
                    # Left Left case; Perform Right rotate to fix it.
                    return self.rotate_right(node)
                elif self.balance_factor(node.left) < 0:
                    # Left Right case; Perform Left rotate then Right rotate to fix it.
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)

        # Right heavy tree
        if bf < -1:
            if node.right:
                if self.balance_factor(node.right) < 0:
                    # Right Right case; Perform Left ritate to fix it.
                    return self.rotate_left(node)
                elif self.balance_factor(node.right) > 0:
                    # Right Left case; Perform Right rotate then Left rotate to fix it.
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)

        return node

    def rotate_left(self, x):
        # prep
        y = x.right
        T2 = y.left

        # perform
        x.right = T2
        y.left = x
        return y

    def rotate_right(self, x):
        # prep
        y = x.left
        T2 = y.right

        # perform
        x.left = T2
        y.right = x
        return y

    def insert_no_return(self, data):
        if not self.root:
            self.root = Node(data)
            self.length += 1
        else:
            self._insert_no_return(data, self.root)
            self.root = self._rebalance(self.root)

    def _insert_no_return(self, data, node):
        if data < node.data:
            if node.left:
                self._insert_no_return(data, node.left)
                node.left = self._rebalance(node.left)
            else:
                node.left = Node(data)
                self.length += 1

        elif data > node.data:
            if node.right:
                self._insert_no_return(data, node.right)
                node.right = self._rebalance(node.right)
            else:
                node.right = Node(data)
                self.length += 1

    def in_order_traversal(self, node=None):
        elements = []
        if self.root is None:
            return None
        if node is None:
            node = self.root

        if node.left:
            elements += self.in_order_traversal(node.left)

        elements.append(node.data)

        if node.right:
            elements += self.in_order_traversal(node.right)

        return elements

    def pre_order_traversal(self, node=None):
        elements = []
        if self.root is None:
            return None
        if node is None:
            node = self.root

        elements.append(node.data)

        if node.left:
            elements += self.pre_order_traversal(node.left)

        if node.right:
            elements += self.pre_order_traversal(node.right)

        return elements

    def post_order_traversal(self, node=None):
        elements = []
        if self.root is None:
            return None
        if node is None:
            node = self.root

        if node.left:
            elements += self.post_order_traversal(node.left)

        if node.right:
            elements += self.post_order_traversal(node.right)

        elements.append(node.data)

        return elements

    def _in_order_successor(self, node):
        if node.right:
            # Case I
            succ = node.right
            while succ.left:
                succ = succ.left
            return succ

        if not node.right:
            # Case II
            p = self.root
            while (p is not None):
                if node.data < p.data:
                    # p is greather than the node; might be the successor
                    succ = p
                    p = p.left
                if node.data > p.data:
                    # p is less than the node; should go right for being greather
                    p = p.right

            return succ

    def is_empty(self):
        return self.root is None

    def is_not_empty(self):
        return self.root is not None

    def height(self):
        return self._height(self.root)

    def _height(self, node=None):
        if self.root is None:
            return None

        if node is None:
            return 0

        return 1 + max(self._height(node.left), self._height(node.right))

    def balance_factor(self, node):
        if node is None:
            node = self.root

        try:
            hl = self._height(node.left)
        except:
            hl = 0

        try:
            hr = self._height(node.right)
        except:
            hr = 0

        return hl-hr

    def __len__(self):
        return self.length

    def _printTree(self, node, level=0):
        if node != None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node)
            self._printTree(node.left, level + 1)

    def print_tree(self):
        self._printTree(self.root)


if __name__ == "__main__":
    A = AVL()
    print(" *** AVL Tree ***")
    data = input("Enter some numbers : ").split()
    data = [int(x) for x in data]
    for d in data:
        A.insert(d)

    print("in_order  --> ", end='')
    print(" ".join(str(x) for x in A.in_order_traversal()))

    print("preorder  --> ", end='')
    print(" ".join(str(x) for x in A.pre_order_traversal()))

    print("postorder --> ", end='')
    print(" ".join(str(x) for x in A.post_order_traversal()))
