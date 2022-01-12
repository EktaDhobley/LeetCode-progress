class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]* (len(triangle) + 1)
        
        for row in triangle[::-1]: #to start from end
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
                
                
        return dp[0]        
    
    #refer Neetcode channel on Yt