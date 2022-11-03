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
        
        
        self.window_sum = 0
        #no. of elements seen so far
        self.count = 0
        
    
    
    def next(self, val: int) -> float:
        
        self.count += 1 #whenever we get to next element (ie what next function is for) increase the count
        
        #cal new sum by shifting the window
        self.q.append(val) #add the new val to deque
        tail = self.q.popleft() if self.count > self.size else 0 #remove the tail from the deque
        
        self.window_sum = self.window_sum - tail + val #remove the tail's value and add new value
        
        return self.window_sum/ min(self.size, self.count)
        
