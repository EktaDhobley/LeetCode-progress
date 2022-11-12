# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
# #         self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0
        #carry shouldn't be 0, if it is we will add it to our output even if l1val and l2val are None, while loop should go on if carry != 0
        while l1 != None or l2 != None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            #new digit
            value = l1val + l2val + carry #15? then we get carry again
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)

            #update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            
        