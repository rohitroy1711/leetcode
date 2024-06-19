# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level = 0
        c = True
        ans = []
        while len(queue)>0:
            for i in range(len(queue)):
                j = queue.popleft()
                if c:
                    ans.append(j.val)
                    c=False
                if j.right:
                    queue.append(j.right)
                if j.left:
                    queue.append(j.left)
            level +=1
            c=True
        return ans