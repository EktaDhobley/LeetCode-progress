class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in dicti:
                return [dicti[comp], i]
            
            dicti[nums[i]] = i
            
        
        