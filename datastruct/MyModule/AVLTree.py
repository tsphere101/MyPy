class NodeAVL:
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
                self.left = NodeAVL(data)
        elif data > self.data[0]:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = NodeAVL(data)

        balance_factor = self.get_balance_factor()
        if balance_factor > 1 and data < self.left.data[0]:
            # left is heavier than right, perfor right rotation
            return self.rotate_right()
        
        if balance_factor > 1 and data > self.left.data[0]:
            # left is heavier than right
            self.left.rotate_left()
            return self.rotate.right()

        if balance_factor < -1 and data > self.right.data[0]:
            # right is heavier than left
            return self.rotate_left()
        if balance_factor < -1 and data < self.right.data[0]:
            self.right.rotate_right()
            return self.rotate_left()

    def rotate_right(self,z):
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3

    def rotate_left(self,z):
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2

    def get_balance_factor(self):
        if self.left:
            left_height = self.left.get_height()
        else:
            left_height = 0
        if self.right:
            right_height = self.right.get_height()
        else:
            right_height = 0

        return left_height - right_height

    def get_height(self):
        if self.left:
            left_height = self.left.get_height()
        else:
            left_height = 0

        if self.right:
            right_height = self.right.get_height()
        else:
            right_height = 0

        child_height = left_height if left_height > right_height else right_height
        return child_height + 1

    def in_order_traversal(self):

        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements += self.data

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def printHelper(self, root, indent, last):
        if root != None:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "
            print(root.data[0])
            self.printHelper(root.left, indent, False)
            self.printHelper(root.right, indent, True)


class AVLTree:
    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            self.root = NodeAVL(data)
        else:
            self.root.add_child(data)

    def __str__(self):
        elements = self.root.in_order_traversal()

        return "[" + ", ".join(str(x) for x in elements)+"]"

    # Print the tree
    def draw_tree(self):
        self.root.printHelper(self.root, "", True)


if __name__ == "__main__":
    a = AVLTree()

    for i in range(6):
        a.append(i)

    print(a)
    print("Height of the tree is :", a.root.get_height())
    print("Balance of the tree is :", a.root.get_balance_factor())
    # a.draw_tree()
