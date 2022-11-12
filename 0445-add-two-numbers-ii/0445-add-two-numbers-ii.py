class Solution:
    def reverseList(self, head):
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp
        
        return last
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        dummy = ListNode()
        curr = dummy
     
        carry = 0
        while l1 or l2 or carry != 0:
            # get the current values 
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            
            # current sum and carry
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
  
            # move to the next elements in the lists
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverseList(dummy.next)