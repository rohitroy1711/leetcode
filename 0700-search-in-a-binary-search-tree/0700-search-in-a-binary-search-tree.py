# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        c = root
        while c:
            if c.val == val:
                return c
            elif val < c.val:
                c = c.left
            else:
                c = c.right
        return None