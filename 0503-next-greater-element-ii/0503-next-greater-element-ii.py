class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        
        for i in list(range(len(nums))) * 2:
            while stack and nums[i] > nums[stack[-1]]:
                val = stack.pop()
                res[val] = nums[i]
            stack.append(i)
            
        return res