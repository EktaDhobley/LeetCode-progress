# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         count = 0
#         res = 0
        
#         start = sorted([i[0] for i in intervals])
#         end = sorted([i[1] for i in intervals])
        
#         s, e = 0, 0
        
#         while s < len(end):
#             if start[s] < end[e]:
#                 s += 1
#                 count += 1
#             else:
#                 e += 1
#                 count -= 1
#             res = max(res, count)    
            
#         return res  
#--------------------------HEAP-------------------------------------
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #error checking
        if not intervals:
            return 0
        
        #sorting acc to start time
        intervals.sort(key = lambda interval : interval[0])
    
        #create heap
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        #iterate throguh all intervals
        
        for interval in intervals[1:]:
            #if no overlap, then pop the min element in heap and push the new end time
            if interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            
        return len(heap)
        
        
        
        
        
        
        
        