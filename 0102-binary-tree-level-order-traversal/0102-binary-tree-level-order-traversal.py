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
        anslis = []
        # level = 0
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            lis = []
            level_size = len(queue)
            for i in range(level_size):
                temp = queue.popleft()
                lis.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            anslis.append(lis)
        return anslis
                
            
        