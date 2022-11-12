"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Two pass solution
        #First pass - for creating copies of each node and mapping original node to corresponding copied node
        #Second pass - leverage hashmap/dictionary to assign random pointers in copied list 
        #Linear time complexity - O(n), even Space Complexity is O(n)
        
        old_to_copy = { None : None }
        
        #first pass
        cur = head
        while cur:
            copy = Node(cur.val) #create new node and copy value
            old_to_copy[cur] = copy #map the old to the copy
            cur = cur.next #move forward
            
        #second pass
        cur = head
        while cur:
            #setting pointers (for random ptrs)
            copy = old_to_copy[cur] #gives copy node of cur
            copy.next = old_to_copy[cur.next] #will give me copy of the next node
            copy.random = old_to_copy[cur.random] #will set pointer of copy to random using cur's random ptr  
            cur = cur.next  #move forward
        return old_to_copy[head]      
        
        
        