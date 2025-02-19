class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

# Helper function to print the tree in-order
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

if __name__ == "__main__":
    # Constructing a sample binary tree:
    #         5
    #        / \
    #       3   8
    #      / \   \
    #     2   4   10
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(10)

    print("BST before insertion:", inorder_traversal(root))
    
    root = insert(root, 7)  # insert new value
    print("BST after insertion:", inorder_traversal(root))
