"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_new_map = {}
        
        def dfs(node):
            if node in old_new_map:
                return old_new_map[node]
            
            else:
                copy = Node(node.val)
                old_new_map[node] = copy #mapping the old to new
                
                for nei in node.neighbors:
                    copy.neighbors.append(dfs(nei))
                return copy
        return dfs(node) if node else None        