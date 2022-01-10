/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
  
         if(head==null)
        {
            return null;
        }
       ListNode prevNode=head;
       ListNode nextNode=prevNode.next;
        
        while(nextNode!=null)
        {
            if(prevNode.val!=nextNode.val)
            {
                prevNode.next=nextNode;
                prevNode=nextNode;
            }
            
            if(nextNode.val==prevNode.val )
            {
                prevNode.next=nextNode.next;
                //nextNode = nextNode.next;
                
            }
            
            nextNode=nextNode.next;
        }
        
        return head;
    }
}