class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # print(len(set(s)))
        # print(len(set(t)))
        # print(set(zip(s, t)))
        # print(len(set(zip(s, t))))
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))