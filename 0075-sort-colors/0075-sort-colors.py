class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        
        
        def swap(a,b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
            
        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            if nums[i] == 2:
                swap(right, i)
                right -= 1
                i -= 1
            i += 1
        