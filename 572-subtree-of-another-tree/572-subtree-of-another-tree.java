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
    public boolean isSubtree(TreeNode root, TreeNode sub) {
        if(root.left==null && root.right==null && sub.left==null && sub.right==null){
            if(root.val!=sub.val)
                return false;
            else
                return true;
        }
        String rootStr = serialize(root);
        String subStr = serialize(sub);
        return rootStr.contains(subStr);
    }
    String serialize(TreeNode root){
        if(root==null) return "#";
        return root.val+","+serialize(root.left)+","+serialize(root.right);
    }
}