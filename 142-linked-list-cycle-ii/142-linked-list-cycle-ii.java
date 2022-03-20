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

public class Solution{
    public ListNode detectCycle(ListNode head){
        Set<ListNode> visited = new HashSet<ListNode>();
        
        ListNode node = head;
        while(node!=null){
            if(visited.contains(node)){
                return node;
            }
            visited.add(node);
            node = node.next;
        }
        return null;
    }
}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
// public class Solution {
//     public ListNode detectCycle(ListNode head) {
//         ListNode fast = head;
//         ListNode slow = head;
        
//         while(fast != null && fast.next != null){
//             slow = slow.next;
//             fast = fast.next.next;
            
//             if(slow == fast){
//                 break;
//             }
//         }
        
//         slow = head;
        
//         while(fast != null && fast.next != null){
//             if(fast == slow){
//                 return fast;
//             }
            
//             fast = fast.next;
//             slow = slow.next;
//         }
        
//         return null;
        
//     }
    
// }