# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        level = 0
        queue.append(root)
        res = []
        while len(queue)>0:
            lis = []
            for i in range(len(queue)):
                j = queue.popleft()
                lis.append(j.val)
                if j.left:
                    queue.append(j.left)
                if j.right:
                    queue.append(j.right)
            res.append(lis)
        return res
                
                    
        