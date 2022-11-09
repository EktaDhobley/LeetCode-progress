"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        dummy = Node(None, None, head, None)
        
        cur, stack = dummy, [head]
        
        while stack:
            tmp = stack.pop()
            if tmp.next: stack.append(tmp.next)
            if tmp.child: stack.append(tmp.child)
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None #because we dont want the child nodes in result
            cur = tmp #move forward
        dummy.next.prev = None #because head's prev is pointed at dummy we dont want that
        return dummy.next
        