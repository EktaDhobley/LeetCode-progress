class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) #intially all are False
        dp[len(s)] = True #dp[last_idx] = True, ie if we ever reach the last index we return True
        
        for i in range(len(s)-1, -1, -1): #Bottom up approach, start from last idx
            for w in wordDict: #go through every word
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w: #
                    dp[i] = dp[i + len(w)]
                    
                if dp[i]:
                    break
        return dp[0]
        