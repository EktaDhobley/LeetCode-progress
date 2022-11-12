class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = float("-inf") #because we have intialise it with some value, cant initialise with 0, since we have negative values
        curSum = 0
        
        for n in nums:
            #if we have a negative sum or negative val, we reset sum to0
            if curSum < 0: 
                curSum = 0
            #otherwise add it to curSum
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
        
         