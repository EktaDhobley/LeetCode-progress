class Solution {
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
}