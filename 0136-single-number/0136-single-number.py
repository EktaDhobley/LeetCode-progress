class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        
        for idx, i in enumerate(nums):
            
            if count[i] < 2:
                ans = i
        return ans