# class Solution:
#     def firstMissingPositive(self, A: List[int]) -> int:
#         #1 - easiest with sorting O(nlogn)
#         A.sort()
#         min = 1
        
#         for i in range(len(A)):
#             if A[i] == min:
#                 min += 1
#         return min
        
# 2 -  using hash set   
class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        y =1
        A = set(A)
        while y in A:
            y+=1
        return y
 
     
# 3- hardest     
# class Solution:
#     def firstMissingPositive(self, A: List[int]) -> int:
        
#         for i in range(len(A)):
#             if A[i] < 0:
#                 A[i] = 0
                
#         for i in range(len(A)):
#             val = abs(A[i])
#             if 1 <= val <= len(A):
#                 if A[val - 1] > 0 :
#                     A[val - 1] *= -1
#                 elif A[val - 1] == 0:
#                     A[val - 1] = -1 * (len(A) + 1)
                    
#         for i in range(1, len(A) + 1):
#             if A[i - 1] >= 0:
#                 return i
#         return len(A) + 1
                
        
        