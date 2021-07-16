""" Python Script to create a binary tree and perform various traversals """

### Write your code from here
##
##class Node:
##    def __init__(self, data):
##        self.left = None
##        self.right = None
##        self.data = data
##
### Insert Node
##    def insert(self, data):
##        if self.data:
##            if data < self.data:
##                if self.left is None:
##                    self.left = Node(data)
##                else:
##                    self.left.insert(data)
##            elif data > self.data:
##                if self.right is None:
##                    self.right = Node(data)
##                else:
##                    self.right.insert(data)
##        else:
##            self.data = data
##
### Print the Tree
##    def PrintTree(self):
##        if self.left:
##            self.left.PrintTree()
##        print(self.data)
##        if self.right:
##            self.right.PrintTree()
##        
##        
##
### Inorder traversal
### Left -> Root -> Right
##    def inorderTraversal(self, root):
##        res = []
##        if root:
##            res = self.inorderTraversal(root.left)
##            res.append(root.data)
##            res = res + self.inorderTraversal(root.right)
##        return res
##
### Preorder traversal
### Root -> Left ->Right
##    def preorderTraversal(self, root):
##        res = []
##        if root:
##            res.append(root.data)
##            res = res + self.preorderTraversal(root.left)
##            res = res + self.preorderTraversal(root.right)
##        return res
### Postorder traversal
### Left ->Right -> Root
##    def postorderTraversal(self, root):
##        res = []
##        if root:
##            res = self.postorderTraversal(root.left)
##            res = res + self.postorderTraversal(root.right)
##            res.append(root.data)
##        return res
##
##root = Node(27)
##root.insert(14)
##root.insert(35)
##root.insert(10)
##root.insert(19)
##root.insert(31)
##root.insert(42)
##
####print("Print the tree: ")
####print(root.PrintTree())
##print("Inorder Travesal: ", root.inorderTraversal(root))
##print("Preorder Travesal: ", root.preorderTraversal(root))
##print("Postorder Travesal: ", root.postorderTraversal(root))


#Using module
from binarytree import tree
#, bst, heap

# Generate a random binary tree and return its root node.
#my_tree = tree(height=2, is_perfect=True)
my_tree_1 = tree()  #--> tree(height=3, is_perfect=False)
### Generate a random BST and return its root node.
##my_bst = bst(height=3, is_perfect=True)
##
### Generate a random max heap and return its root node.
##my_heap = heap(height=3, is_max=True, is_perfect=False)
##
### Pretty-print the trees in stdout.
print(my_tree_1)
print(my_tree_1.properties)
##print(my_bst)
##print(my_heap)
##
####
####       _3___
####      /     \
####  ___12     _7
#### /         /  \
####14        10   13
####  \
####   2
####
####
####        ______7_______
####       /              \
####    __3__           ___11___
####   /     \         /        \
####  1       5       9         _13
#### / \     / \     / \       /   \
####0   2   4   6   8   10    12    14
####
####
####         _______14______
####        /               \
####    ___13__            __12__
####   /       \          /      \
####  11        9        7        10
#### /  \      / \      / \      /  \
####4    2    3   8    6   0    5    1



