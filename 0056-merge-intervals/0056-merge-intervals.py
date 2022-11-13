class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        intervals.sort(key = lambda x : x[0]) #sorting according to the start values
        res = [intervals[0]] #putting first interval in the output
        
        for start, end in intervals[1:]: #intervals start from 1,cuz we added 0th interval in output
            lastEnd = res[-1][1] #-1 means get most recent element and 1 means end value of array
            
            if start <= lastEnd: # checking start of next interval with end of last interval(merge possible)
                res[-1][1] = max(lastEnd, end) #[1,5] [2,4] we want max(4,5)
            else: #when non-overlapping #[1,5] [7,8]
                res.append([start,end])
                
        return res            