# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 #number of elements visited in bst
        stack = []
        curr = root
        
        while curr or stack:
            while curr: #while cur is not null
                stack.append(curr) #store the value of curr in stack
                curr = curr.left #keep going left until you encounter a null
            curr = stack.pop()  #we set the most recently added elem from stack to cur
            #we are popping it hence we are processing it, hence we increase 'n'
            n += 1
            
            if n == k:
                return curr.val
            curr = curr.right  
            
            
         
            