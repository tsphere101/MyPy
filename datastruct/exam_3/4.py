class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_bst(list_nums, node=None):
    if node is not None:
        if list_nums[0] <= node.val:
            if node.left:
                node.left = list_to_bst(list_nums, node.left)
            else:
                node.left = TreeNode(list_nums.pop(0))

        elif list_nums[0] > node.val:
            if node.right:
                node.right = list_to_bst(list_nums, node.right)
            else:
                node.right = TreeNode(list_nums.pop(0))

        bf = balance_factor(node)
        # print("BALANCE FACTOR",bf)

        if bf > 1:
            if node.left:
                if balance_factor(node.left) > 0:
                    return rotate_right(node)
                elif balance_factor(node.left) < 0:
                    node.left = rotate_left(node.left)
                    return rotate_right(node)

        if bf < -1:
            if node.right:
                if balance_factor(node.right) < 0:
                    return rotate_left(node)
                elif balance_factor(node.right) > 0:
                    node.right = rotate_right(node.right)
                    return rotate_left(node)

        return node

    # Iterate through lists
    else:
        for i in range(len(list_nums)):
            if i == 0:
                root = TreeNode(list_nums.pop(0))
            else:
                # data = list_nums[0]
                root = list_to_bst([(list_nums.pop(0))],root)


                # if data < root.val:
                #     if root.left:
                #         root.left = list_to_bst([list_nums.pop(0)], root.left)
                #     else:
                #         root.left = TreeNode(list_nums.pop(0))
                # elif data > root.val:
                #     if root.right:
                #         root.right = list_to_bst([list_nums.pop(0)], root.right)
                #     else:
                #         root.right = TreeNode(list_nums.pop(0))

        bf = balance_factor(root)

        if bf > 1:
            if root.left:
                if balance_factor(root.left) > 0:
                    # Left Left case; Perform Right rotate to fix it.
                    root = rotate_right(root)
                elif balance_factor(root.left) < 0:
                    # Left Right case; Perform Left rotate then Right rotate to fix it.
                    root.left = rotate_left(root.left)
                    root = rotate_right(root)

        if bf < -1:
            if root.right:
                if balance_factor(root.right) < 0:
                    # Right Right case; Perform Left ritate to fix it.
                    root = rotate_left(root)
                elif balance_factor(root.right) > 0:
                    # Right Left case; Perform Right rotate then Left rotate to fix it.
                    root.right = rotate_right(root.right)
                    root = rotate_left(root)
                    # return rotate_left(node)

        return root


def balance_factor(node):
    if node.left:
        hl = height_of_node(node.left)
    else:
        hl = 0

    if node.right:
        hr = height_of_node(node.right)
    else:
        hr = 0

    bf = hl - hr

    return bf


def height_of_node(node):
    if node.left:
        hl = height_of_node(node.left)
    else:
        hl = 0

    if node.right:
        hr = height_of_node(node.right)
    else:
        hr = 0

    return 1 + max(hl, hr)


def rotate_left(node):
    y = node.right
    T2 = y.left

    node.right = T2
    y.left = node
    return y


def rotate_right(x):
    y = x.left
    T2 = y.right

    x.left = T2
    y.right = x
    return y


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
