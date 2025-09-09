# Step 1: Define the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Step 2: Implement the Binary Search Tree Class with all methods
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Step 3: Implement the Insertion Method
    def insert(self, value):
        if self.root is None:
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

    # Step 4: Implement the Search Method
    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)

    # Step 5: Implement Traversal Methods
    def inorder_traversal(self):
        result = []
        self._inorder_recursively(self.root, result)
        return result

    def _inorder_recursively(self, node, result):
        if node:
            self._inorder_recursively(node.left, result)
            result.append(node.value)
            self._inorder_recursively(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursively(self.root, result)
        return result

    def _preorder_recursively(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursively(node.left, result)
            self._preorder_recursively(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursively(self.root, result)
        return result

    def _postorder_recursively(self, node, result):
        if node:
            self._postorder_recursively(node.left, result)
            self._postorder_recursively(node.right, result)
            result.append(node.value)

    # Step 6: Implement the Deletion Method
    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children
            min_node = self._min_value_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursively(node.right, min_node.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Additional methods
    def find_max(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.value

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def level_order_traversal(self):
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_valid_bst(self):
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))

    def _is_valid_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return self._is_valid_bst(node.left, min_val, node.value) and self._is_valid_bst(node.right, node.value, max_val)

# Test code
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test search
print(bst.search(4)) # Should return a Node
print(bst.search(9)) # Should return None

# Test traversals
print("In-order:", bst.inorder_traversal())   
print("Pre-order:", bst.preorder_traversal())
print("Post-order:", bst.postorder_traversal())

# Test deletion
bst.delete(3)
print("In-order after deleting 3:", bst.inorder_traversal())

# Test new methods
print("Maximum value:", bst.find_max())
print("Total nodes:", bst.count_nodes())
print("Level-order traversal:", bst.level_order_traversal())
print("Height:", bst.height())
print("Is valid BST:", bst.is_valid_bst())
