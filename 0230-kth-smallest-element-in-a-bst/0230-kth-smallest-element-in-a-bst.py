# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The below method is to making the tree into a inorder list and then printing out the ith index from the list. 
        lis = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            lis.append(root.val)
            inorder(root.right)
        inorder(root)
        return lis[k-1]
