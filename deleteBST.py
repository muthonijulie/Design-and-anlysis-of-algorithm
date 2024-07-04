class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # A utility function to insert a new node with the given key
    def insert(self, node, key):
        # If the tree is empty, return a new node
        if node is None:
            return Node(key)

        # Otherwise, recur down the tree
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)

        # return the (unchanged) node pointer
        return node

    # A utility function to do inorder traversal of BST
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Given a binary search tree and a key, this function deletes the key and returns
    # the new root
    def deleteNode(self, root, key):
        # Base case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left
        # subtree
        if key < root.key:
            root.left = self.deleteNode(root.left, key)

        # If the key to be deleted is greater than the root's key, then it lies in the right
        # subtree
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)

        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right
            # subtree)
            root.key = self.minValue(root.right)

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.key)

        return root

    def minValue(self, root):
        minv = root.key
        while root.left:
            minv = root.left.key
            root = root.left
        return minv

# Driver Code
if __name__ == "__main__":
    tree = BinaryTree()

    # Let us create following BST
    #
    #     50
    #    /  \
    #   30   70
    #  / \  / \
    # 20 40 60 80

    tree.insert (tree.root, 50)
    tree.insert(tree.root, 30)
    tree.insert(tree.root, 20)
    tree.insert(tree.root, 40)
    tree.insert(tree.root, 70)
    tree.insert(tree.root, 60)
    tree.insert(tree.root, 80)

    print("Original BST:", end=" ")
    tree.inorder(tree.root)
    print()

    print("\nDelete a Leaf Node: 20")
    tree.root = tree.deleteNode(tree.root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    tree.inorder(tree.root)
    print()

    print("\nDelete Node with single child: 70")
    tree.root = tree.deleteNode(tree.root, 70)
    print("Modified BST tree after deleting single child Node:")
    tree.inorder(tree.root)
    print()

    print("\nDelete Node with both child: 50")
    tree.root = tree.deleteNode(tree.root, 50)
    print("Modified BST tree after deleting both child Node:")
    tree.inorder(tree.root)
