# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
#         n = 0
#         stack = []
#         curr = root
        
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             n += 1
            
#             if n == k:
#                 return curr.val
#             curr = curr.right # since we have popped the curr from stack, we can now visit itss right subtree
            
        n = 0 #number of elements visited in bst
        stack = []
        curr = root
        
        while curr or stack:
            while curr: #while cur is not null
                stack.append(curr) #store the value of curr in stack
                curr = curr.left #keep going left until you encounter a null
            curr = stack.pop()  #we set the most recently added elem from stack to curr
            #we are popping it hence we are processing it, hence we increase 'n'
            n += 1
            
            if n == k:
                return curr.val
            else:
                curr = curr.right  #if n != k, after processing the curr, go to its right subtree, and enter the outer while loop again, since we have popped the curr from stack, we can now visit its right subtree
            
            
            
         
            