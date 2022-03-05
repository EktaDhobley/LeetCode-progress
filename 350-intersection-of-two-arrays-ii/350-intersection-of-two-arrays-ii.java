class Solution {
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
    
}
