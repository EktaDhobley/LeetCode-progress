// TC. - O(n+m)
// SC - O(min(n,m))

/* class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
    
    if (nums1.length > nums2.length) {
        return intersect(nums2, nums1); 
    } 
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    for(Integer n : nums1){
        map.put(n, map.getOrDefault(n,0) + 1);
    }
        int k = 0;
        for(Integer i : nums2){
            int m = map.getOrDefault(i,0);
            if(m > 0){
                map.put(i, m-1);
                nums1[k++] = i;
            }
                
            }
        
        return Arrays.copyOfRange(nums1, 0, k);
    }
    
} */

// Sorting approach
//TC - O(nlogn + mlogm)
//SC - O(nlogn + mlogm)
class Solution{
    public int[] intersect(int nums1[] , int nums2[]){
       
        
        int i = 0 , j = 0, k = 0;
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
      while(i < nums1.length && j < nums2.length){
          if( nums1[i] == nums2[j]){
              nums2[k++] = nums1[i++];
              j++;
          }
          else if(nums1[i] < nums2[j]){
              i++;
          }
          else{
              j++;
          }
      }
        return Arrays.copyOfRange(nums2, 0, k);
    }
}