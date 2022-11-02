
//DP Solution
// class Solution {
//     public int maxSubArray(int[] nums) {
//        int maxSum = nums[0];
//        int curr = nums[0];
        
//        for(int i = 1 ; i < nums.length ; i++){
//            int num = nums[i];
           
//            curr = Math.max( num, curr + num);
//            maxSum = Math.max(maxSum, curr);
//        } 
        
//         return maxSum;
        
//     }
// }


//Sliding window
class Solution{
    public int maxSubArray(int[] nums){
        int curr = 0;
        int maxSum = nums[0];
        
        for(int i = 0; i < nums.length; i++){
            if(curr < 0){
                curr = 0;
            }
             
            curr = curr + nums[i];
            maxSum = Math.max(maxSum, curr);
            
        }
      return maxSum;  
    }
    
}