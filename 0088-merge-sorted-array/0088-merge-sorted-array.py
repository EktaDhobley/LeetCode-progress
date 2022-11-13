class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #last idx of nums1
        
        last = n + m - 1
        #merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        #fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
            
            
    
   #-------------------------------------------------------------------          
        # for i in range(n):
        #     nums1[i + m] = nums2[i]  
        # nums1.sort()
   #-------------------------------------------------------------------     
        # nums1_copy = nums1[:m] #make a copy of nums1 with only elements that are non-zero
        # x,y = 0, 0
        # for p in range(n + m): #iterate throughout n+m = len(nums1)
        #     if y >= n or (x < m and nums1_copy[x] <= nums2[y]): #check if x and y are not out of range
        #         nums1[p] = nums1_copy[x] #place the lower value in the nums1 copy
        #         x += 1
        #     else:
        #         nums1[p] = nums2[y]
        #         y += 1
        
 #-------------------------------------------------------------------    

        #last idx of nums1
    
            