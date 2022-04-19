class Solution {
    public int maxSubArray(int[] nums) {
       int maxSum = nums[0];
       int curr = nums[0];
        
       for(int i = 1 ; i < nums.length ; i++){
           int num = nums[i];
           
           curr = Math.max( num, curr + num);
           maxSum = Math.max(maxSum, curr);
       } 
        
        return maxSum;
        
    }
}