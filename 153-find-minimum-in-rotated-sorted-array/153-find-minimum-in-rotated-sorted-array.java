// class Solution {
//     public int findMin(int[] nums) {
//         if(nums.length == 1){
//             return nums[0];
//         }
        
//         int end = nums.length-1;
//         int start = 0;
        
//         if(nums[end] > nums[0]){
//             return nums[0];
//         }
        
//         while(start <= end){
//             int mid = start + (end - start)/2 ; //straight forward easy
//             if(nums[mid] > nums[mid + 1]){
//                 return nums[mid+1];
//             }
//             else if(nums[mid] < nums[mid - 1]){ //straight forward easy
//                 return nums[mid];
//             }
            
//             if(nums[mid] > nums[0]){ //if nums[mid] > nums[0] that means we have to search on right of nums[mid] inorder to find the min element
//                 start = mid + 1;
//             }
//             else{ //if nums[mid] > nums[0] that means we have to search on left of nums[mid] inorder to find the min element
//                 end = mid - 1;
//             }
//         }
//         return -1;
//     }
// }

class Solution {
    public int findMin(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        
       
        int start = 0;
        int end = nums.length - 1;
        
         if(nums[end] > nums[0]){
            return nums[0];
        } //Not rotated
        
    
        
        while(start <= end){
            int mid = start + (end-start)/2;
            
            if(nums[mid] > nums[mid + 1]){
                return nums[mid+1];
            }
            else if( nums[mid] < nums[mid - 1] ){
                return nums[mid];
            }
            else if(nums[mid] > nums[0]){
                start = mid+1;
            }
            else{
                end = mid-1;
            }
        }
        return -1;
    }
        
    }