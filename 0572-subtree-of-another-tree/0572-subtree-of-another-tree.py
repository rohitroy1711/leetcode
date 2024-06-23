# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self,root,subRoot)->bool:
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val!= subRoot.val:
                return False
            return self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right) 
            
        #The Below is the code where it finds the sub tree if there are any identical nodes else it returns false
#         if not root or not subRoot:
#             return False
        
#         def findSubInRoot(subRoot,root)->Optional[TreeNode]:
#             if not root:
#                 return None
#             if subRoot.val == root.val:
#                 return root
#             node = findSubInRoot(subRoot,root.left)
#             node_r = findSubInRoot(subRoot,root.right)
#             return node or node_r 
        
#         sub_node = findSubInRoot(subRoot,root)
        
        
        
#         def checkSubTree(sub_node,subRoot)->bool:
#             if not sub_node and not subRoot:
#                 return True
#             if not sub_node or not subRoot or sub_node.val != subRoot.val :
#                 return False
#             return (checkSubTree(sub_node.left,subRoot.left) and checkSubTree(sub_node.right,subRoot.right))
        
        
#         if sub_node == None:
#             return False
#         else:
#             return checkSubTree(sub_node,subRoot)