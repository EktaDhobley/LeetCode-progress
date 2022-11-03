# class MovingAverage:
    
#     #size = 3 for 1st example
#     def __init__(self, size: int):
#         self.size = size
#         self.q = []
        

#     def next(self, val: int) -> float:
#         size, q = self.size, self.q
#         q.append(val)
        
#         window_sum = sum(q[-size:])
        
#         return window_sum/min(len(q),size)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
class MovingAverage:
    
    def __init__(self, size: int):
        self.size = size
        self.q = collections.deque()
        
        #no. of elements seen so far
        self.window_sum = 0
        self.count = 0
        
    
    
    def next(self, val: int) -> float:
        
        self.count += 1
        
        #cal new sum by shifting the window
        self.q.append(val)
        tail = self.q.popleft() if self.count > self.size else 0
        
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum/ min(self.size, self.count)
        
