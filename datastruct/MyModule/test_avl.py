class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class AVL:
    def __init__(self) -> None:
        self.root = None
        self.lenght = 0
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(data,self.root)

    def _insert(self,data,node):
        if data < node.data:
            if node.left:
                node.left = self._insert(data,node.left)
                return node
            else:
                node.left = Node(data)
                return node

        elif data > node.data:
            if node.right:
                node.right = self._insert(data,node.right)
                return node

            else:
                node.right = Node(data)
                return node

        return node
        
    def get_height(self,node):

        if node.left:
            hl = self.get_height(node.left)
        else:
            hl =0
        
        if node.right:
            hr = self.get_height(node.right)
        else:
            hr = 0

        return 1+ max(hl,hr)

    def in_order_traversal(self,node=None):
        if node is None:
            return self.in_order_traversal(self.root)

        elements = []
        if node.left:
            elements+= self.in_order_traversal(node.left)
        elements+= [node.data]

        if node.right:
            elements+= self.in_order_traversal(node.right)
        
        return elements
    

if __name__ == "__main__":
    
    a = AVL() 

    a.insert(5)
    a.insert(2)
    a.insert(3)

    print(a.in_order_traversal())
        
    print(a.get_height(a.root.left))