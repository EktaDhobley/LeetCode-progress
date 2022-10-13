class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Method 1 : Sorting
        
        if len(s) != len(t):
            return False
        count = 0
        sorted_s = ''.join(sorted(s)) #sorted and changed back to string by using join
        sorted_t = ''.join(sorted(t))
        
        for x, y in zip(sorted_s, sorted_t):
            if x == y:
                count += 1
        return count == len(sorted_s)        
        #return filter(lambda (x,y) : x == y , zip (sorted_s, sorted_t))
        #return filter(lambda (x, y): x == y, zip(sorted_s, sorted_t))