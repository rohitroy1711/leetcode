# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sume: int) -> bool:
        if not root:
            return False
        sume = sume-root.val
        if sume == 0 and root.left == None and root.right == None:
            return True
        if self.hasPathSum(root.left,sume):
            return True
        if self.hasPathSum(root.right,sume):
            return True
        return False
        