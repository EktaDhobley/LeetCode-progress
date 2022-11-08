# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
        
#         for i in range(len(temperatures)):
#             for j in range(i + 1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     res[i] = j - i
#                     break
#         return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return ans