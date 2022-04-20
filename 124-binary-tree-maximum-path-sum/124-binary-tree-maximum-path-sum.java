/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    int res = Integer.MIN_VALUE;
    
    public int helper(TreeNode node){
        if(node == null) return 0;
    
    
    int left_sum = helper(node.left);
    int right_sum = helper(node.right);
    left_sum = Math.max(left_sum , 0);
    right_sum = Math.max(right_sum , 0);
    
    int price_newpath = node.val + left_sum + right_sum;
    
    res = Math.max(res, price_newpath);
    
    return node.val + Math.max(left_sum, right_sum);
    }   
    public int maxPathSum(TreeNode root) {
        
        helper(root);
        return res;
        
    }
         
    }
