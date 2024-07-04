class TreeNode:
    def __init__(self, key: int):
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.val: int = key

def inorder_traversal(root: TreeNode | None):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# Creating a binary search tree
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Inorder traversal:")
inorder_traversal(root)
print()
