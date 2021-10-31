class Node:
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
        self.left = None
        self.right = None

    def is_leaf(self):
        return not self.left and not self.right


class AVL:

    def __init__(self):
        self.root = None

    def insert(self, data, pos):
        if self.root is None:
            self.root = Node(data, pos)

        else:
            self.root = self._insert(data, pos, self.root)

    def _insert(self, data, pos, node):
        if not node.left:
            node.left = Node(data, pos)
            return node
        if not node.right:
            node.right = Node(data, pos)
            return node

        if node.left.is_leaf() or not self.isPerfect(node.left):
            node.left = self._insert(data, pos, node.left)
            return node

        if node.right.is_leaf() or not self.isPerfect(node.right):
            node.right = self._insert(data, pos, node.right)
            return node

        node.left = self._insert(data, pos, node.left)
        return node

    def search_for_pos(self, pos, node=None):
        if node is None:
            node = self.root

        if node.pos == pos:
            return node

        if node.left:
            node_found = self.search_for_pos(pos, node.left)
            if node_found:
                return node_found

        if node.right:
            node_found = self.search_for_pos(pos, node.right)
            if node_found:
                return node_found

    def sum_node(self, node):
        result = 0
        result += node.data

        if node.left:
            result += self.sum_node(node.left)

        if node.right:
            result += self.sum_node(node.right)

        return result

    # Returns depth of leftmost leaf.
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

    # Wrapper over isPerfectRec()
    def isPerfect(self, root):
        d = self.findADepth(root)
        return self.isPerfectRec(root, d)

    def power_of_troop(self, pos):
        return self.sum_node(self.search_for_pos(pos))


if __name__ == "__main__":

    t = AVL()
    powers, pairs = input("Enter Input : ").split("/")

    powers = [int(x) for x in powers.split()]

    for i, data in enumerate(powers):
        t.insert(data, i)

    print(t.sum_node(t.root))

    for data in pairs.split(","):
        first = int(data.split()[0])
        second = int(data.split()[1])

        if t.power_of_troop(first) > t.power_of_troop(second):
            operator = '>'

        elif t.power_of_troop(first) < t.power_of_troop(second):
            operator = '<'
        else:
            operator = '='

        print(f"{first}{operator}{second}")
