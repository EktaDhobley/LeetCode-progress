class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        result = 0
        
        count = Counter(nums)
        
        for x in count:
            if k > 0 and x + k in count:
                result += 1
            if k == 0 and count[x] > 1:
                result += 1
        return result