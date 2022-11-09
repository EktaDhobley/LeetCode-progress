class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        h = []
        
        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]