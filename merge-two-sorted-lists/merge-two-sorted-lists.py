# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # method 1 - recursion
        # if list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        # elif list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
        
        #method 2 - iteration
        dummy = ListNode(-1)
        pre = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next    
        pre.next = list1 if list1 is not None else list2
        return dummy.next
            
        
        