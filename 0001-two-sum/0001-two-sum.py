class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#     #one pass hashmap/ dictionary   
#     dicti = {}
        
#         for i in range(len(nums)):
#             comp = target - nums[i]
            
#             if comp in dicti:
#                 return [dicti[comp], i]
            
#             dicti[nums[i]] = i
            
        hashmap = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in hashmap and hashmap[comp] != i:
                return [hashmap[comp], i]
            #index daalo map mein har number ka
            hashmap[nums[i]] = i
        
        
        
        
        #two pass hashmap/dcitionary

#         dicti = {}
        
#         for i in range(len(nums)):
#             dicti[nums[i]] = i 
            
#         for i in range(len(nums)):
#             comp = target - nums[i]
            
#             if comp in dicti and dicti[comp] != i:
#                 return [i, dicti[comp]]