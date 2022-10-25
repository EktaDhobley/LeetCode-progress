class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Input: nums = [0,0,0,3,12]
        # Output: [1,3,12,0,0]
        a = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[a], nums[i] = nums[i], nums[a]
                a += 1
        
                
        