# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            right_side = None
            q_len = len(q) #length of current queue
            
            for i in range(q_len):
                node = q.popleft() #pop the left element and store it in node
                if i == q_len - 1:
                        right_side = node 
                    
                if node:
                    if node.left: #if node is not null, add its children
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
    
                
            if right_side:
                res.append(right_side.val)
                
            
                
        return res
        