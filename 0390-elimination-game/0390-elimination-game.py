#https://www.youtube.com/watch?v=e0Og3BhJAe0
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return n
        
        else:
            return 2*(n//2 - self.lastRemaining(n//2) + 1)
        