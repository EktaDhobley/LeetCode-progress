//Solution 1 
// O(n^2)
/* class Solution {
    public int[] twoSum(int[] nums, int target) {
        
       // int arr[] = new int[2];
        for(int i = 0 ; i < nums.length; i++ ){
            for(int j = i+1 ; j< nums.length ; j++ ){
                if(nums[j] == target - nums[i]){
                   return new int[] {i,j};
            }
        }
    }
          return null;
        }
       
    }
*/

// O(n)
class Solution{
    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> map = new HashMap(nums.length);
        int ans[] = new int[2];
        for(int i = 0 ; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                ans[0] = map.get(target-nums[i]);
                ans[1] = i;
            }
            map.put(nums[i], i);
        }
        return ans;
    }
} 

// O(nlogn)
// class Solution{
//     public int[] twoSum(int[] nums, int target){
//         int sorted[] = Arrays.copyOf(nums, nums.length);
        
//         int low = 0;
//         int high = nums.length-1;
//         int sum = sorted[low] + sorted[high];
//         int a = 0;
//         int b = 0;
//         int arrSorted[] = new int[2];
//         while(low<high){
//             if(sum == target){
//             arrSorted[0] = sorted[low];
//             arrSorted[1] = sorted[high];
//         }
//         else if(sum < target){
//             low++;
//         }
//         else{
//             high--;
//         }
//         }
        
//         int arr[] = new int[2];
//         for(int i = 0 ; i < nums.length; i++){
//             if(nums[i] == arrSorted[0]){
//                 arr[0] = i;
//             }
//         }
//         for(int i = 0 ; i < nums.length; i++){
//             if(nums[i] == arrSorted[1]){
//                 arr[1] = i;
//             }
//         }
//         return arr;
        
//     }
// }



















