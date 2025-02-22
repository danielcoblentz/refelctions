class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# return the minimum value node of the BST
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# remove a node and return the root of the BST
def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

# Helper function to print the tree in-order
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

if __name__ == "__main__":
    if __name__ == "__main__":
    # constructing a sample binary tree
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

    print("BST before delete operation:", inorder_traversal(root))
    
    root = remove(root, 10)  # remove node
    print("BST after delete operation:", inorder_traversal(root))