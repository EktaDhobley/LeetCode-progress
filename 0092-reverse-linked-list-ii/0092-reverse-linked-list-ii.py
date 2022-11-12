# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        
        leftPrev, curr = dummy, head
        
        for i in range(left - 1):
            leftPrev = curr
            curr = curr.next
            
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy = ListNode(0, head) #created dummy node which points at head
        
#         leftPrev = dummy
#         cur = head
        
#         # 1) reach node at position "left"
#         for i in range(left - 1): #2-1 times iterate to reach left
#             leftPrev = cur
#             cur = cur.next
            
#         # 2) Now cur = "left", leftPrev = "node after left"
#         # reverse from left to right
#         prev = None
#         for i in range(right - left + 1):
#             tmpNext = cur.next
#             cur.next = prev
#             prev = cur
#             cur = tmpNext
        
#         # 3) Update pointers
#         leftPrev.next.next = cur
#         leftPrev.next = prev
        
#         return dummy.next
            
        
        