class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for n in arr:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif abs(n - x) < abs(heap[0] - x):
                heappushpop(heap, n)
        return sorted(heap)