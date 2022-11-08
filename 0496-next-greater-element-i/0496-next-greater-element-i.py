#brute force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                
                if nums2[j] == nums1[i]:
                    found = True
                    
                if found and nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break 
            #after for loop if j reaches end of array 
            # if j == len(nums2):
            #     res[i] = -1
                    
        return res
            
            
#stack and map
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    