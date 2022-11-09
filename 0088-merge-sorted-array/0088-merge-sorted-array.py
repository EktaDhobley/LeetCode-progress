class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[i + m] = nums2[i]  
        # nums1.sort()
        
        nums1_copy = nums1[:m] #make a copy of nums1 with only elements are non-zero
        x,y = 0, 0
        for p in range(len(nums1)): #iterate throughout n+m 
            if y >= n or (x < m and nums1_copy[x] <= nums2[y]): #check if x and y are not out of range
                nums1[p] = nums1_copy[x] #place the lower value in the nums1 copy
                x += 1
            else:
                nums1[p] = nums2[y]
                y += 1