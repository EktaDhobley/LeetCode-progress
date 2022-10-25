class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#     #one pass hashmap/ dictionary   
#     dicti = {}
        
#         for i in range(len(nums)):
#             comp = target - nums[i]
            
#             if comp in dicti:
#                 return [dicti[comp], i]
            
#             dicti[nums[i]] = i
            
        
        #two pass hashmap/dcitionary

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
#         dicti = {}
        
#         for i in range(len(nums)):
#             dicti[nums[i]] = i 
            
#         for i in range(len(dicti)):
#             comp = target - nums[i]
            
#             if comp in dicti and dicti[comp] != i:
#                 return [i, dicti[comp]]