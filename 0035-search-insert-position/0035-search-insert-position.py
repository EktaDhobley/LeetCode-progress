class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) #target could be bigger than the last value in the array
        
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
        