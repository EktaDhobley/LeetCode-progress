class MovingAverage:
    
    #size = 3 for 1st example
    def __init__(self, size: int):
        self.size = size
        self.q = []
        

    def next(self, val: int) -> float:
        size, q = self.size, self.q
        q.append(val)
        
        window_sum = sum(q[-size:])
        
        return window_sum/min(len(q),size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)