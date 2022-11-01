# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         def helper(node, left, right):
#             if not node:
#                 return True
            
#             if not (node.val < right and node.val > left):
#                 return False
            
#             return (helper(node.left, left, node.val) and helper(node.right, node.val, right)) #boundaries for left and right using parent's limiting values
        
#         return helper(root, float("-inf"), float("inf"))
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = -math.inf
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if root.val <= prev:
                return False
            else:
                prev = root.val
                root = root.right
        return True