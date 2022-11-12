# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         nodes_visited = set()
#         while head is not None: #If the current node is null, we have reached the end of the list and it must not be cyclic
#             if head in nodes_visited:
#                 return True
#             nodes_visited.add(head)
#             head = head.next
#         return False    

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False