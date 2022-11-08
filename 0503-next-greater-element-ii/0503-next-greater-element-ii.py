# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         stack = []
#         res = [-1] * len(nums)
        
#         for i in list(range(len(nums))) * 2:
#             while stack and nums[i] > nums[stack[-1]]:
#                 val = stack.pop()
#                 res[val] = nums[i]
#             stack.append(i)
            
#         return res
    
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums) # taking an empty stack for storing index, a list with the lenght same as of nums so that we wont add unnecessary elements.
        # [-1] * len(nums) = this will produce a list with len of nums and all elems will be -1.
        for i in list(range(len(nums))) * 2: # see explanation below.
            while stack and (nums[stack[-1]] < nums[i]): # stack is not empty and nums previous elem is less then current, i.e 1<2. 
                res[stack.pop()] = nums[i] # then we`ll pop the index in stack and in the res on the same index will add the current num. 
            stack.append(i) # if stack is empty then we`ll add the index of num in it for comparision to the next element in the provided list. 
        return res # returing the next greater number for every element in nums.