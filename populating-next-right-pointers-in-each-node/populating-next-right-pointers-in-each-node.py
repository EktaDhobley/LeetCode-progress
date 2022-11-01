"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        cur = root
        nxtlevel = root.left if root else None 
        
        while cur and nxtlevel:
            cur.left.next = cur.right #connect the left and right children
            if cur.next: #if there is a node next of cur, then connect right of cur to left of cur's next (level 2 in the above example)
                cur.right.next = cur.next.left 
            
            cur = cur.next #point to next node if there exists a next for cur, else it is null
            if not cur: #if cur is null, go to next level
                cur = nxtlevel
                nxtlevel = cur.left
         
        return root
        