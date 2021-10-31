# ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k

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

    def count_if_less_than_or_eq(self, node, data):
        if self.root:

            if node is None:
                return 0

            if node.data <= data:
                count = 1 + self.count_if_less_than_or_eq(node.left, data) + self.count_if_less_than_or_eq(node.right, data)

            else:
                count = self.count_if_less_than_or_eq(node.left, data)

            return count

        else:
            return 0

    def __str__(self):
        if self.root != None:
            level = 0
            self.printTree(self.root.right, self.root + 1)
            print('     ' * level, self.root)
            self.printTree(self.root.left, level + 1)


if __name__ == "__main__":
    tree = BST()
    numbers, value = input("Enter Input : ").split("/")
    numbers = [int(x) for x in numbers.split()]
    value = int(value)

    for data in numbers:
        tree.insert(data)

    tree.printTree(tree.root)

    print("--------------------------------------------------")

    print(tree.count_if_less_than_or_eq(tree.root, value))
