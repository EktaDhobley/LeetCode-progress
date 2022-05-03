class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #ending of new interval is less than starting of one of the intervals
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: #start of new interval is greater than end of one of the intervals
                res.append(intervals[i])
            else: #when intervals are overlapping, we will merge the intervals
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)       #incase first if doesn't execute
        return res
    
                
                
        
        
        