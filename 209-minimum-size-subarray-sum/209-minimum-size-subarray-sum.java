class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int left=0;
        int val_sum=0;
        int result=Integer.MAX_VALUE;
            
            for(int i=0;i<nums.length;i++){
                val_sum=val_sum+nums[i];
                
                while(val_sum>=s){
                    result=Math.min(result, i+1-left); //i=3, left=0 ( for 1st testcase) ( to find the left of the subarrray)
                    val_sum=val_sum-nums[left]; //left=0;
                    left++;
                } 
            }    
     return (result!=Integer.MAX_VALUE)? result : 0;
    
    }
}