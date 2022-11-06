# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        ans = 0
        
        while q:
            list_nodes = []
            
            for i in range(len(q)):
                node, idx = q.popleft()
                list_nodes.append(idx) #indexes of all nodes at a level
                
                if node.left:
                    q.append((node.left, 2 * idx + 1))
                if node.right:
                    q.append((node.right, 2 * idx + 2))
                
            ans = max(ans, max(list_nodes) - min(list_nodes) + 1)
                
            
        return ans