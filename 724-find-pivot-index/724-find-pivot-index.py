class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = 0
        left_sum = 0
        
        for i in range(len(nums)):
            summ += nums[i]
        for i in range(len(nums)):
            if left_sum == summ - left_sum - nums[i]:
                return i
            left_sum += nums[i]
            
        
        return -1