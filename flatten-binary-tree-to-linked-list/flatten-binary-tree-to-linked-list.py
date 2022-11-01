# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #this function will flaten the root tree and return list tail
        def dfs(root):
            if not root:
                return None
            
            leftTail = dfs(root.left) #flatten left subtree
            rightTail = dfs(root.right) #flatten right subtree
            
            if leftTail: #if leftTail is not null, then insert it (because even if righttail is not null, we dont care as righttail is on right only, we dont need to change anything there)
                leftTail.right = root.right #insert the left tail,ie attach th tail to right of root
                root.right = root.left #attach root's right to root's left 
                root.left = None #question says we dont need any left subtrees
                
            last = rightTail or leftTail or root #order of this matters     
            return last      
        dfs(root) #we dont have to return anything