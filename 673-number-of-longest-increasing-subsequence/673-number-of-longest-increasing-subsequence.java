 class Solution{
     public int findNumberOfLIS(int[] nums) {
        int[] lis = new int[nums.length+1];
        int[] count = new int[nums.length+1];
        // [1] is 1 size long LIS, counts as one too
        Arrays.fill(lis, 1);
        Arrays.fill(count, 1);
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    
                    if (lis[j] + 1 > lis[i]) {  // new longest case for lis[i]
                        lis[i] = lis[j] + 1;
                        count[i] = count[j];
                        
                    } else if (lis[j] + 1 == lis[i])    // equal longest case for lis[i]
                        count[i] += count[j];
                }
            }
        }
        
        // find longest LIS from DP and return its count
        int longest = 0;
        for (int n : lis) longest = Math.max(longest, n);
        int res = 0;
        for (int i = 1; i < nums.length+1; i++)
            if (lis[i] == longest)
                res += count[i];
        return res;
    }
}