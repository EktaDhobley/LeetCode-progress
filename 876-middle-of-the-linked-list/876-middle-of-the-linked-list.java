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
    public ListNode middleNode(ListNode head) {
       int length=0;
        ListNode p=head;
        ListNode q=head;
        while(q!=null){
            q=q.next;
            length++;
        }
        if(length%2==0){
            for(int i=0;i<length/2; i++){
                p=p.next;
            }
        }
        else if(length%2!=0){
            for(int i=0;i<(length-1)/2;i++){
                p=p.next;
            }
        }
        return p;
    }
}