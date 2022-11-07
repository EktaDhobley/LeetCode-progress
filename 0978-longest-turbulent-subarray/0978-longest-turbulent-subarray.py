class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
       
        def isCurrIndexTurbulent(A, k):
            return A[k] > A[k-1] and A[k] > A[k+1] or A[k] < A[k-1] and A[k] < A[k+1]
        
        if len(A) < 2:
            return len(A)
        
        maximum = 1
        start, end = 0, 0
        N = len(A)
        
        while start + 1 < N:
            if A[start] == A[start + 1]:
                start+=1
                continue
            end = start + 1
            while end + 1 < N and isCurrIndexTurbulent(A, end):
                end += 1
                
                
            maximum = max(maximum, end - start + 1)
            start = end #for next subarray check
            
        return maximum
    
    