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
   
     /*  List<List<Integer>> levels = new ArrayList<List<Integer>>();
        
        public void helper( TreeNode node, int level ){
            //starting the current level
            if(levels.size() == level)
                levels.add(new ArrayList<Integer>());
            
            //fulfil the current level
            levels.get(level).add(node.val);
            
            //processing child nodes for the next level   
            if(node.left!= null)
                helper(node.left, level + 1);
            if(node.right != null)
               helper(node.right, level + 1);
        }
    }  
        public List<List<Integer>> levelOrder (TreeNode root){
            if(root == null) return levels;
            helper(root, 0);
            return levels; */
        
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        
        
        public void helper(TreeNode root, int level){
            if(list.size() == level){
            list.add(new ArrayList<Integer>());
        }
            list.get(level).add(root.val);
            
            if(root.left!= null)
                helper(root.left, level +1);
            if(root.right!=null)
                helper(root.right, level + 1);
        }
        
 public List<List<Integer>> levelOrder(TreeNode root) {
     if(root == null) return list;
      helper(root, 0);
     return list;
        }
}