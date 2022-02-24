class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keep_track = dict()
        
        for i, j in enumerate(nums):
            
            value = target - j
            
            if value in keep_track:
                return [keep_track[value],i]
            keep_track[j] = i
            
            
  