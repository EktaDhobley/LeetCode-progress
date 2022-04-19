

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2){
        
        ListNode head;
        
        if ( l1 == null){
            return l2;
        }
        else if ( l2 == null){
            return l1;
        }
        
        else if(l1.val < l2.val){
            //l1.next = mergeTwoLists(l1.next, l2);
            head = l1;
            l1 = l1.next;
            
        }
        else {
            head = l2;
            l2 = l2.next;
        }
        
        head.next = mergeTwoLists(l1, l2);
        return head;
    }
}