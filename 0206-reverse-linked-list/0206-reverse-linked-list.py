# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##recursive
        #base case
        if head is None: #null
            return head
        if head.next is None:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
    #recursive explained here - https://www.youtube.com/watch?v=S92RuTtt9EE
        
#         #iterative
#         prev = None
#         curr = head
        
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         return prev       
        
            

        
          