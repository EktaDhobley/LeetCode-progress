class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                 # check if we have enough characters starting from i in string s to compare with w, if they are, we compare
                if (i + len(w)) <= len(s) and s[i : i+ len(w)] == w:
                    dp[i] = dp[i + len(w)] #dp[0] = d[0 + len(w)] = True, since dp[4] = True (len(w) = 4)
                if dp[i]: # we found the word, now break, and move on to next word
                    break
        return dp[0]
            
        