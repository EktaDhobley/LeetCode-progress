from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) #we remove left elemnets frm set as long as we have s[r] in our set (that means its a duplicate)
                l += 1
            charSet.add(s[r])
            res =  max(res, r - l + 1)
            
        return res