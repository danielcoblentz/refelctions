from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Breadth-First Search (Level Order Traversal)
def bfs(root):
    if not root:
        return
    
    queue = deque([root])  # Initialize queue with the root node
    
    while queue:
        node = queue.popleft()  # Dequeue the front node
        print(node.val)  # Process the current node
        
        if node.left:
            queue.append(node.left)  # Enqueue left child
        
        if node.right:
            queue.append(node.right)  # Enqueue right child

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

    print("BFS Level Order Traversal:")
    bfs(root)
