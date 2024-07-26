"""
B016 - https://leetcode.com/problems/increasing-order-search-tree/description/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root):
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        node.left = None
        self.curr.right = node
        self.curr = node
        inorder(node.right)

    dummy = TreeNode()
    self.curr = dummy
    inorder(root)
    return dummy.right
