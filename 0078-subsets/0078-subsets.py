# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         output = [[]]
        
#         for n in nums:
#             output = output + [curr + [n] for curr in output]
        
#         return output
class Solution:
     def subsets(self, nums: List[int]) -> List[List[int]]:
            res = [] #list
            
            subset = [] #array
            
            def dfs(i): #i is index of nums
                if i >= len(nums): #out of bounds we have reached our leaf nodes 
                    res.append(subset.copy())
                    return
                
                #decision to include nums[i] #left decisoion
                subset.append(nums[i])
                dfs(i + 1) #this call will have a different subset given to it
                
                #decision not to include nums[i] #right
                subset.pop() #pop the elements just appended
                dfs(i + 1) #this dfs call will get an empty subset passed to it
                
            dfs(0)
            return res