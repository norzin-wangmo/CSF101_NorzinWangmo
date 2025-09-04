#Step 1: Define the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 2: Implement the Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None

#Step 3 : Implement the Insertion Method
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)
# Test insertion
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Step 4: Implement the Search Method
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search_recursively(self.root, value)
    
    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)
    
# Test search
print(bst.search(4)) # Should return a Node
print(bst.search(9)) # Should return None

# Step 5: Implement Traversal Methods

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self):
        result = []
        self._inorder_recursively(self.root, result)