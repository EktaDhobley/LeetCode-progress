/*class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0 ; i < len; i++){
            set.add(nums[i]);
           
        }
        int k = -1;
        for(int i = 0 ; i <= len ; i++){
            if(!set.contains(i)){
                k = i;
            }
        }
         return k;
    }
} */

class Solution{
    public int missingNumber(int[] nums){
        Arrays.sort(nums);
        int len = nums.length;
       if(nums[len-1] != nums.length){
           return len;
       }
        else if(nums[0] != 0){
            return 0;
        }
        
        for(int i = 1 ; i < nums.length; i++){
            int k = nums[i-1] + 1;
            if(nums[i] != k){
                return k;
            }
            
        }
        
        return -1;
        
    }
}