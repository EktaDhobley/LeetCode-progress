# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         # print(len(set(s)))
#         # print(len(set(t)))
#         # print(set(zip(s, t)))
#         # print(len(set(zip(s, t))))
#         return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        return True