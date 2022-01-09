# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            if curr.val == val:
                if prev: #when middle element is unwanted
                    prev.next = curr.next
                else: #when prev is at None, that is first elememnt is unwanted
                    head = curr.next
                curr = curr.next
            else: #when no element is unwanted
                prev = curr
                curr = curr.next
                
        return head
        

        
        
