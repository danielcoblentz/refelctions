# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# preorder: (V, L, R)
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# inorder: (L, V, R)
def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# postorder: (L, R, V)
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

if __name__ == "__main__":
    # Constructing a sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Preorder traversal:")
    preorder(root)
    
    print("\nInorder traversal:")
    inorder(root)
    
    print("\nPostorder traversal:")
    postorder(root)
