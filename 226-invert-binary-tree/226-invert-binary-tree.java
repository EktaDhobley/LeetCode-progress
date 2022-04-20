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
 
 public TreeNode invertTree(TreeNode root) {
        if(root == null) {
            return root;
        }
        if(root.left == null && root.right ==null) {
            return root;
        }
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        TreeNode temp;
        if(root == null ) return null;
        
        //if(root.left==null && root.right==null) return root;
        
        
            temp = root.left;
            root.left = root.right;
            root.right = temp;
        
            invertTree(root.left);
            invertTree(root.right);
        
        return root;
    }
}