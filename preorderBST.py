class TreeNode:
  def __init__(self, key):
       self.left: TreeNode | None = None
       self.right: TreeNode | None = None
       self.val: int = key
def preorder_traversal(root):
  if root:
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)
# Creating a binary search tree
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
print("Preorder traversal:")
preorder_traversal(root)
print()