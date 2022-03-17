/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */


//Approach 1
public class Solution{
    public boolean hasCycle(ListNode head){
        Set<ListNode> set = new HashSet<>();
        while(head!=null){
            if(set.contains(head)){
                return true;
            }
            set.add(head);
            head = head.next;
        }
        return false;
    }
}





/* Approach 2
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast=head;
        ListNode slow=head;
        
        if(head == null) return false;
        
     while(fast.next != null && fast.next.next !=null)   {
        fast=fast.next.next;
        slow=slow.next;
     
        if(fast == slow) 
        {
            return true;
        } 
     }
        return false;
        
    }
} */