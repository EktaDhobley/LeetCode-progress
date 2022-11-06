# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if not head or not head.next:
#             return head
        
#         odd = head
#         even = head.next
#         even_head = even
        
#         while odd and even and even_head:
#             odd.next = even.next
#             odd = odd.next
#             if odd:
#                 even.next = odd.next
#                 even = even.next
            
#         odd.next = even_head
        
#         return head
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head_even, odd, even = head.next, head, head.next
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next

        odd.next = head_even
        return head       
        
    
            