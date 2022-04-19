# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
        
#         if len(nums) == 0:
#             return 0
        
#         res = nums[0]
#         for i in range(len(nums)):
#             acc = 1
            
#             for j in range(i, len(nums)):
#                 acc = acc * nums[j]
#                 res = max(res, acc)
                
         
#         return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        
        max_sofar = nums[0]
        min_sofar = nums[0]
        res = max_sofar
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_sofar * curr, min_sofar * curr)
            min_sofar = min(curr, max_sofar * curr, min_sofar * curr)
            
            max_sofar = temp_max
            
            res = max(max_sofar, res)
            
            
        return res    
        
        
        
        
        