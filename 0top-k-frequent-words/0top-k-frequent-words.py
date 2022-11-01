#from heapq import nsmallest

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        return nsmallest(k, counts.keys(), key = lambda x : (-counts[x], x))
        