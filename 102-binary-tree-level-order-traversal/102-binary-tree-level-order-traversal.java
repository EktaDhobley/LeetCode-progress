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
   
        
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        
        public void helper(TreeNode node, int level){
            if(list.size() == level)
                list.add(new ArrayList<Integer>()); //just when we go to next level we will check this condition because thats when we will need a new arraylist to add elements to it.
                list.get(level).add(node.val);
                
                //for left
                
                if(node.left != null){
                    helper(node.left, level + 1);
                }
                
                
                //for right
                if(node.right != null){
                    helper(node.right, level + 1);
                }
                
            
        }
        
        
         public List<List<Integer>> levelOrder(TreeNode root) {
             if(root == null) return list;
             
             helper(root, 0);
             return list;
    }
}