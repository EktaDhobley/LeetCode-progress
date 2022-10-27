class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        output = []
        l, r = 0, 0
        
        while r < len(nums): #r should not go out of bounds
            while q and nums[q[-1]] < nums[r]:
                #remove the smaller value and then add the bigger value
                q.pop()
            q.append(r)
            
            
            #remove left from window to maintain size of k
            if l > q[0]:
                q.popleft()
                
            if (r + 1) >= k : #should at least be of window size k
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output            
                