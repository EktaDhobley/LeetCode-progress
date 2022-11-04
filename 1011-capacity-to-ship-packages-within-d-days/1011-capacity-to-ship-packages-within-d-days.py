class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(capacity):
        
            D = 1
            total = 0
            
            for w in weights:
                total += w
                
                if total > capacity: #wait for next day
                    total = w
                    D += 1
                    
                    if D > days:
                        return False
            return True
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
                    