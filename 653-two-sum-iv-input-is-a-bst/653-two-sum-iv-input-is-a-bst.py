# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        ht = set()
        def helper(root): 
            if root: 
                calcValue = k - root.val
                if calcValue in ht: 
                    return True 
                else:
                    ht.add(root.val)
                    
                return helper(root.left) or helper(root.right) 
                
        return helper(root)