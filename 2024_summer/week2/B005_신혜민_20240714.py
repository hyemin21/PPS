class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root: TreeNode, k: int) -> bool:
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    
    nums = inorder(root)
    l, r = 0, len(nums) - 1
    
    while l < r:
        s = nums[l] + nums[r]
        if s == k:
            return True
        elif s < k:
            l += 1
        else:
            r -= 1
    return False
