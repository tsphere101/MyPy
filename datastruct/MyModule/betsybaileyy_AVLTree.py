class AVLTreeNode(object):
    
    def __init__(self, data):
        """Initialize this avl tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        """Return a string representation of this avl tree node."""
        return 'AVLTreeNode({!r})'.format(self.data)
    
    def contains_left_node(self):
        """Returns true/false if there is a left node"""
        if self.left == None:
            return False
        else:
            return True

    def contains_right_node(self):
        """Returns true/false if there is a right node"""
        if self.right == None:
            return False
        else:
            return True

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        if self.left or self.right:
            return False
        else:
            return True

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        if self.left or self.right:
            return True
        else:
            return False

    def get_balance(self):
        '''Similar to get height, if a None child is passed,
        its children are equally balanced so balance factor is 0'''
        if self.is_leaf():
            return 0
        elif self.contains_right_node() == False:
            return-self.left.height - 1
        elif self.contains_left_node() == False:
            return self.right.height + 1
        else:
            return self.right.height - self.left.height

    def get_height(self):
        '''calculate/update node height'''
        if self.is_leaf():
            self.height = 0
        elif not self.contains_left_node():
            self.height = self.right.height + 1
        elif not self.contains_right_node():
            self.height = self.left.height + 1
        else:
            if self.left.height > self.right.height:
                self.height = self.left.height + 1
            else:
                self.height = self.right.height + 1
        
    def add_height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        if self.is_leaf():
            self.height = 0
        elif not self.contains_left_node():
            self.height = self.right.height + 1
        elif not self.contains_right_node():
            self.height = self.left.height + 1
        else:
            if self.left.height > self.right.height:
                self.height = self.left.height + 1
            else:
                self.height = self.right.height + 1

    def left_rotation(self):
        ''' Set the original root as the left child of the original roots right
        child. Then return the original roots right child as the new root. '''
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        self.get_height()
        right_child.get_height()
        return right_child

    def right_rotation(self):
        # Same as left_rotation just reversed
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        self.get_height()
        left_child.get_height()
        return left_child
 


class AVLTree(object):

    def __init__(self, items=None):
        """Initialize this AVL tree and insert the given items."""
        # self.root = AVLTreeNode(1000000)
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    # Thank you to Alan Davis for this print sting function!!!!!!!
    def __str__(self, node=None):
        """Return a visual string representation of this binary search tree.
        Performs depth-first traversal starting at the given node or root."""
        if node is None:
            if self.is_empty():  # Special case
                return 'root -> None'
            else:  # Start recursion at root node
                return '\n'.join(self.__str__(self.root))
        strings = []  # Accumulate separate strings since we need to pad them
        if node.right is not None:  # Descend right subtree, if it exists
            for right_string in self.__str__(node.right):
                # Left-pad strings and replace ambiguous root with right link
                strings.append(5 * ' ' + right_string.replace('->', '/-', 1))
        strings.append('-> ({})'.format(repr(node.data)))  # This node's string
        if node.left is not None:  # Descend left subtree, if it exists
            for left_string in self.__str__(node.left):
                # Left-pad strings and replace ambiguous root with left link
                strings.append(5 * ' ' + left_string.replace('->', '\\-', 1))
        return strings

    def __repr__(self):
        """Return a string representation of this AVL tree."""
        return 'AVLTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node)."""
        # Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this tree contains the given item."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this tree matching the given item,
        or None if the given item is not found."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node else None

    

    def insert(self, item, node=None):
        """Insert the given item in order into this tree."""
        if self.is_empty():
            self.root = AVLTreeNode(item)
            self.size += 1
            return

        if node is None:
            node = self.root
            self.size += 1

        if item == node.data:
            self.size -= 1
            return
        elif item < node.data:
            if node.contains_left_node():
                added_subtree = self.insert(item, node.left)
                if added_subtree is not None:
                    node.left = added_subtree
            else:
                added_node = AVLTreeNode(item)
                node.left = added_node
        else:
            if node.contains_right_node():
                added_subtree = self.insert(item, node.right)
                if added_subtree is not None:
                    node.right = added_subtree
            else:
                added_node = AVLTreeNode(item)
                node.right = added_node
        node.get_height()
        return self.balance(node)

    def balance(self, node):
        bf = node.get_balance()
        if bf < 2 and bf > -2: 
            return None
        if bf < -1:
            if node.left.get_balance() < 0:
                new_root = node.right_rotation()
            else:
                node.left = node.left.left_rotation()
                new_root = node.right_rotation()
        else:
            if node.right.get_balance() > 0:
                new_root = node.left_rotation()
            else:
                node.right = node.right.right_rotation()
                new_root = node.left_rotate()
        if node is self.root:
            self.root = new_root
        return new_root
        


    def _find_node_iterative(self, item):
        """Return the node containing the given item in this tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node."""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node."""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            # Hint: Remember to update the parent parameter
            return self._find_parent_node_recursive(item, node=node.left, parent=node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            # Hint: Remember to update the parent parameter
            return self._find_parent_node_recursive(item, node=node.right, parent=node)


    def items_in_order(self):
        """Return an in-order list of all items in this tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        # Traverse left subtree, if it exists
        if node is not None:
            if node.left:
                self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right:
            self._traverse_in_order_recursive(node.right, visit)

    def items_pre_order(self):
        """Return a pre-order list of all items in this tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        # Visit this node's data with given function
        if node is not None:
            visit(node.data)
        # Traverse left subtree, if it exists
            if node.left:
                self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
            if node.right:
                self._traverse_pre_order_recursive(node.right, visit)

    def items_post_order(self):
        """Return a post-order list of all items in this tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        # Traverse left subtree, if it exists
        if node is not None:
            if node.left:
                self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
            if node.right:
                self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)


    def items_level_order(self):
        """Return a level-order list of all items in this AVL search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this AVL tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function."""
        # Create queue to store nodes not yet traversed in level-order
        queue = Queue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right:
                queue.enqueue(node.right)
    
    # def printTree(self):
    #     PrintBTree(self,lambda n:(str(n.value),n.left,n.right))      



# root.addValue(50)
# root.addValue(90)
# root.addValue(10)
# root.addValue(60)
# root.addValue(30)
# root.addValue(70)
# root.addValue(55)
# root.addValue(5)
# root.addValue(35)
# root.addValue(85)

# root.printTree()

def test_AVL_tree():
    # Create a complete AVL search tree of 3, 7, or 15 items in level-order
    # items = [7, 2, 6, 1, 3, 5, 4]
    # items = ['betsy', 'erica', 'nya', 'faith', 'jasmine', 'stephanie',]
    # items = [4,2,6,1,3,5,7]
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # root = AVLTreeNode(items)
    # for item in items:
    #     tree.insert(item)
    print('items: {}'.format(items))

    tree = AVLTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))
    print(tree)
    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    
    print('items level-order: {}'.format(tree.items_level_order()))

    print(tree)

if __name__ == '__main__':

    # We are using a list of our classmates as the input 
    # to demonstrate our AVL Tree's functionality:
    students = ['Ali', 'Betsy', 'Cherish', 'Erica', 'Ikey', 'Jackson', 
    'Jake', 'Javier', 'Jayce', 'KJ', 'Luc', 'Lucia', 'Makhmud', 'Drew', 
    'Nathan', 'Nolan', 'Ruhsane', 'Ryan', 'Sam', 'Sukhrob', 'Thomas', 'Zurich']
    
    # Now, we call AVLTree and pass in 'students' as the parameter.
    # Then, we set the AVLTree this equal to a variable 'tree'. 
    tree = AVLTree(students)

    # Once we run 'python3 avl_tree.py' in our terminal, we should see a
    # balanced tree structure containing each student's name stored as a node.
    print(tree)
   






      # items = ['betsy', 'erica', 'nya', 'faith', 'jasmine', 'stephanie',]
     # items = [1,2,3,4,5,6,7,8,9]