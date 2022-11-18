class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        
        for n in nums:
            if n in num_map:
                return True
            
            else:
                num_map[n] = 1
        return False