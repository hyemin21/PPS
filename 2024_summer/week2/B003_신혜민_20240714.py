class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    
    def is_leaf(node):
        return node and not node.left and not node.right
    
    def dfs(node):
        if not node:
            return 0
        if is_leaf(node.left):
            return node.left.val + dfs(node.right)
        return dfs(node.left) + dfs(node.right)
    
    return dfs(root)
