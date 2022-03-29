// class Solution {
//     public int[] searchRange(int[] nums, int target) {
//         int result[] = new int[]{-1,-1};
        
//         if(nums == null || nums.length == 0){
//             return result;
//         }
        
        
//         result[0] = findLeft(nums, target);
//         result[1] = findRight(nums, target);
//         return result;
//     }
        
//         private int findLeft(int[] nums, int target){
//             int left = 0; 
//             int right = nums.length - 1;
//             while(left + 1 < right){
//                  int mid = left + (right-left)/2;
//                 if(nums[mid] < target){
//                     left = mid;
//                 }
//                 else{
//                     right = mid;
//                 }
//              }
            
//             if(nums[left] == target){
//                 return left;
//             }
//             else if(nums[right]== target){
//                 return right;
//             }
//             return -1;
//         }
        
//          private int findRight(int[] nums, int target){
//             int left = 0; 
//             int right = nums.length - 1;
//              while(left + 1 < right){
//                  int mid = left + (right-left)/2;
//                  if(nums[mid] <= target){
//                      left = mid;
//                  }
//                  else{
//                      right = mid;
//                  }
//              }
//             if(nums[right] == target){
//                 return right;
//             }
//              else if(nums[left] == target){
//                  return left;
//              }
//              return -1;
//         }
        
// }


class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        if(nums.length == 0 || nums == null) return new int[]{-1,-1};
        
        int arr[] = new int[2];
        arr[0] = -1;
        arr[1] = -1;
        
        int i = 0;
        int j = nums.length - 1;
        
        while( i <= j){
            if(nums[i] < target){
                i++;
            }
            else if (nums[j] > target){
                j--;
            }
            else if(nums[i] == target && nums[j] == target)
                return new int[]{i,j};
            
        }
        
        return arr;
        
}


}