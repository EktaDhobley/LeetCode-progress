# #brute force
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = [-1]*len(nums1)
        
#         for i in range(len(nums1)):
#             found = False
#             for j in range(len(nums2)):
                
#                 if nums2[j] == nums1[i]:
#                     found = True
                    
#                 if found and nums2[j] > nums1[i]:
#                     res[i] = nums2[j]
#                     break #break from j for loop, because we found the greater number and added to res, now we will iterate i 
    
#         return res
            
            
#stack and map
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        nums1_idx = { n:i for i, n in enumerate(nums1)} #for storing index of each number of nums1
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_idx[val]
                res[idx] = cur
            if cur in nums1_idx: #check if cur is in nums1 then only append to stack, otherwise we dont care
                stack.append(cur) 
        
        return res
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    