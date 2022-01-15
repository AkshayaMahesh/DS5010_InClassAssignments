#Part 1
# Creating a class Node and it's attributes
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
#Part 2
# Creating a class BinaryTree and it's attributes
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)
#Part 3
# Creating a method to compute the inorder traversal
    def print_inorder(self,start,traversal):
        if start:
            traversal=self.print_inorder(start.left,traversal)
            traversal = traversal + str(start.value) + ' '
            traversal = self.print_inorder(start.right, traversal)
        return traversal
# Part 4
# Creating a tree along with the node values
tree=BinaryTree('D')# Root Node
tree.root.left=Node('B')
tree.root.right=Node('F')
tree.root.left.left=Node('A')
tree.root.left.right=Node('C')
tree.root.right.left=Node('E')
tree.root.right.right=Node('G')
#Part 5
# Testing the created method using the print function
print("Inorder Traversal result: ",tree.print_inorder(tree.root,' '))