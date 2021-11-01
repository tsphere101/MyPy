class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return not self.left and not self.right

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, n, data):
        self.root = None
        self.size = 0

        threshold = int(n/2)
        for i in range(n):
            if len(self) < threshold:
                self.insert(None)
            else:
                self.insert(data.pop(0))

    def findADepth(self, node):
        d = 0
        while (node != None):
            d += 1
            node = node.left
        return d

    def isPerfectRec(self, root, d, level=0):

        # An empty tree is perfect
        if (root == None):
            return True

        # If leaf node, then its depth must
        # be same as depth of all other leaves.
        if (root.left == None and root.right == None):
            return (d == level + 1)

        # If internal node and one child is empty
        if (root.left == None or root.right == None):
            return False

        # Left and right subtrees must be perfect.
        return (self.isPerfectRec(root.left, d, level + 1) and
                self.isPerfectRec(root.right, d, level + 1))

    def isPerfect(self, root):
        d = self.findADepth(root)
        return self.isPerfectRec(root, d)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size += 1
        else:
            self.root = self._insert(data, self.root)
            self.size += 1

    def _insert(self, data, node):
        if not node.left:
            node.left = Node(data)
            return node
        if not node.right:
            node.right = Node(data)
            return node

        if node.left.is_leaf() or not self.isPerfect(node.left):
            node.left = self._insert(data, node.left)
            return node

        if node.right.is_leaf() or not self.isPerfect(node.right):
            node.right = self._insert(data, node.right)
            return node

        bf = self.balance_factor(node)
        if bf > 0:
            node.right = self._insert(data, node.right)
            return node

        node.left = self._insert(data, node.left)
        return node

    def balance_factor(self, node):

        if node.left:
            hl = self.height(node.left)
        else:
            hl = 0

        if node.right:
            hr = self.height(node.right)
        else:
            hr = 0

        return hl-hr

    def height(self, node):
        if node.left:
            hl = self.height(node.left)
        else:
            hl = 0

        if node.right:
            hr = self.height(node.right)
        else:
            hr = 0

        return 1+max(hl, hr)

    def kill_rude_tree(self):
        if self.root is None:
            return
        else:
            self.root = self._kill_rude_tree(self.root)

    def _kill_rude_tree(self, node):
        if node.is_leaf():
            # Base case
            return node

        if node.left and node.right:
            node.left = self._kill_rude_tree(node.left)
            node.right = self._kill_rude_tree(node.right)

            value = min(node.left.data, node.right.data)

            node.data = value
            node.left.data -= value
            node.right.data -= value

            return node

    def sum_node(self, node=None):
        if self.root is None:
            return 0

        if node is None:
            node = self.root

        if node.left:
            left_sum = self.sum_node(node.left)
        else:
            left_sum = 0

        if node.right:
            right_sum = self.sum_node(node.right)
        else:
            right_sum = 0

        return node.data + left_sum + right_sum

    def _printTree(self, node, level=0):
        if node != None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node)
            self._printTree(node.left, level + 1)

    def print_tree(self):
        self._printTree(self.root)

    def __len__(self):
        return self.size


if __name__ == "__main__":

    amount, data = input("Enter Input : ").split("/")

    amount = int(amount)
    data = [x for x in map(int, data.split())]

    # CHECK ARGUMENTS FIRST
    if int(amount/2) + 1 != len(data):
        print("Incorrect Input")
        exit()

    t = Tree(amount, data)

    for d in data:
        t.insert(d)

    t.kill_rude_tree()
    print(t.sum_node())
