class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_bst(list_nums):
    if list_nums == []: return
    middle_index = len(list_nums)//2
    node = TreeNode(list_nums[middle_index])
    try:
        node.left = list_to_bst(list_nums[:middle_index])
    except IndexError:
        pass
    try:
        node.right = list_to_bst(list_nums[middle_index+1:])
    except IndexError:
        pass
    return node


def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


def printBST(node, level=0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.val)
        printBST(node.left, level + 1)


list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums)


print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)
