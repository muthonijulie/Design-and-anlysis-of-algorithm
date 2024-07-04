class TreeNode:
  def __init__(self, key):
     self.left: TreeNode | None = None
     self.right: TreeNode | None = None
     self.val: int = key
def postorder_traversal(root):
   if root:
      postorder_traversal(root.left)
      postorder_traversal(root.right)
      print(root.val, end=' ')
# Creating a binary search tree
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)
print("Postorder traversal:")
postorder_traversal(root)
print()