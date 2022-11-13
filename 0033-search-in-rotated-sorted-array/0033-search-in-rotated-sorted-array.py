# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         l, r = 0, len(nums) - 1
        
#         while l <= r:
#             mid = (l+r) // 2
#             if target == nums[mid]:
#                 return mid
            
#             #left sorted array
#             if nums[l] <= nums[mid]: #to check if we are in left sorted array of right
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#            #right sorted array
#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1
        
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            #
            if target == nums[mid]:
                return mid
            
            #check if in left sorted array
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            #right sorted array
            elif nums[right] > nums[mid]:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        