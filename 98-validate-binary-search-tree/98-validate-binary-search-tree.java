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
    public boolean isValidBST(TreeNode root) {
        return isBSTUtil(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    boolean isBSTUtil(TreeNode root, long minValue, long maxValue){
        if(root==null) return true;
        
        if(root.val>minValue && root.val< maxValue && isBSTUtil(root.left, minValue, root.val) && isBSTUtil( root.right, root.val, maxValue))
            return true;
        
        else
            return false;
    }
}