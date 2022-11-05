class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #using set
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                
                while (n + length) in num_set:
                    length += 1 #if the numbers in the sequence moving forward are present in the set
                
                longest = max(length, longest)
        return longest