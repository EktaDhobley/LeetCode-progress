//Solution 1 
/* class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int arr[] = new int[2];
        for(int i =0 ; i < nums.length; i++ ){
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

class Solution{
    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> map = new HashMap(nums.length);
        int ans[] = new int[2];
        for(int i = 0 ; i < nums.length; i++){
            if(map.containsKey(target - nums[i])){
                ans[0] = map.get(target-nums[i]);
                ans[1] = i;
                map.clear();
                return ans;
            }
            map.put(nums[i], i);
        }
        return ans;
    }
}