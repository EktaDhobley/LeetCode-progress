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
    public ListNode removeElements(ListNode head, int val) {
      
  ListNode ptr = head;
        while(head!=null && ptr.val==val) {
            head = ptr.next;
            ptr = ptr.next;
        }
      
          if(head==null)
            return head; 
        while(ptr.next!=null) {
            if(ptr.next.val==val)
                ptr.next = ptr.next.next;
            else
                ptr = ptr.next;
        }
        return head;
    } 
}