# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         res = []
        
#         nums.sort()
        
#         left, right = 0, len(nums) - 1
#         while left <= right:
            
#             mid =  right - left // 2
            
#             if target == nums[mid]:
#                 if nums[left] < target:
#                     left += 1
#                 if nums[right] > target:
#                     right -= 1
#                 if nums[left] == target and nums[right] == target:
#                     res.append(left)
#                     left += 1
#             if target < nums[mid]:
#                 right = mid - 1
#             elif target > nums[mid]:
#                 left = mid + 1
#         return res
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = []
            
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            
            elif nums[mid] == target:
                if nums[l]<target:
                    l = l + 1
                if nums[r]>target:
                    r = r -1 
                if nums[l]==target and nums[r]==target:
                    res.append(l)
                    l+=1

        return res