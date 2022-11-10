class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        #[rob1, rob2, n, n + 1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 #for next value where we want to do rob2, hence change rob1 = rob2
            rob2 = temp #and get max in rob2 #up until now
            
        return rob2        