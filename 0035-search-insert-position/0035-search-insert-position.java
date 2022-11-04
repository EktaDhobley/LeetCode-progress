class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int pos = nums.length;
        for(int i=0;i<nums.length-1;i++){
               if(nums[i]==target) pos=i;
        else if(nums[i]< target && target<=nums[i+1])
                pos= i+1;
        }
        
       if(target<=nums[0])
                pos=0;
        
        
    return pos;
    }
}