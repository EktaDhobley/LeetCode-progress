class Solution:
    def firstUniqChar(self, s: str) -> int:
        #building hashmap
        
        count = collections.Counter(s)
        
        #find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1    