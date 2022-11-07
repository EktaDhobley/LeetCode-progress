class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # sort in-place
        # keep numbers in ascending order
        nums.sort()
        
        # counter for valid triplet to make triangle
        valid_triplet = 0
        
        for index_i in range( len(nums)-1, 1, -1):
            
            k = nums[index_i]
            
            i, j = 0, index_i - 1
            
            while i < j:
                
                i_ = nums[i]
                j_ = nums[j]
                
                if i_ + j_ > k:
                    
                    # valid triplets
                    # first_edge    : from nums[i] to nums[(j-1)]
                    # second edge   : nums[j]
                    # third edge    : nums[index_i]
                    valid_triplet += ( j - i )
        
                    # second edge large enough
                    # make it smaller and try next run
                    j -= 1
                else:
                    # first edge is too small
                    # make it larger and try next run
                    i += 1
        
        
        
        return valid_triplet
        