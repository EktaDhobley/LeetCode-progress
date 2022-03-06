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
/*class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode third=null;
        ListNode last=null;
        
        if(l1.val<=l2.val){
            third=l1;
            last=l1;
            l1=l1.next;
            last.next=null;
        }
        else if(l2.val<=l1.val){
            third=l2;
            last=l2;
            l2=l2.next;
            last.next=null;
        }
   while(l1!=null && l2!=null){     
        if(l1.val<l2.val){
            last.next=l1;
            last=l1;
            l1=l1.next;
            last.next=null;
        }
        else if(l1.val>=l2.val)
        {
            last.next=l2;
            last=l2;
            l2=l2.next;
            last.next=null;
        }
   }
        if(l1!=null) {
            last.next=l1;
        }
        else { 
            last.next=l2;
        }
    return third;
    }
} */

 class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }
        
        
        ListNode tmp = new ListNode();
        ListNode result = tmp;
        
        int data;
        while(l1 != null && l2 != null){
            if(l1.val >= l2.val){
                data = l2.val;
                l2 = l2.next;
            }else{
                data = l1.val;
                l1 = l1.next;
            }
            tmp.next = new ListNode(data);
            tmp = tmp.next;
        }
        
        while(l1 != null){
            tmp.next = new ListNode(l1.val);
            tmp = tmp.next;
            l1 = l1.next;
        }
         while(l2 != null){
            tmp.next = new ListNode(l2.val);
            tmp = tmp.next;
            l2 = l2.next;
        }
        
        return result.next;
        
    }
} 