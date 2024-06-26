# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,currSum):
            if not root:
                return False
            currSum += root.val
            if root.left == None and root.right == None:
                return currSum == targetSum
            
            if dfs(root.left,currSum):
                return True
            #currSum -= root.val
            if dfs(root.right,currSum):
                return True
            return False
        
        return dfs(root,0)