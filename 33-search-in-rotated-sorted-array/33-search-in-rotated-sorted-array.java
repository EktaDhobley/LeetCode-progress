class Solution {
    public int search(int[] nums, int target) {
         int left = 0, right = nums.length - 1;        
        while(left <= right) {
            int mid = (left + right) / 2;
            if(nums[left] == target) {
                return left;
            } else if(nums[mid] == target) {
                return mid;
            } else if(nums[right] == target) {
                return right;
            } else if(nums[left] > target) {
                if( nums[mid] > target && nums[mid] < nums[left]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }              
            } else if(nums[left] < target){ 
                if(nums[mid] < target && nums[mid] > nums[left]) {
                    left = mid + 1;
                } else  {
                    right = mid - 1;
                }           
            }
        }
        return -1;
    }
}