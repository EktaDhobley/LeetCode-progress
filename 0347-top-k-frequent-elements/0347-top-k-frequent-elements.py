# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count_map = {} #Map to map frequencies to elements
#         freq = [[] for i in range(len(nums) + 1)] #to store frequency of each value
        
#         for n in nums:
#             count_map[n] = 1 + count_map.get(n, 0) #counting the numbe rof frequencies
#         for n, c in count_map.items(): #mapping frequencies to value
#             freq[c].append(n)
            
#         res = [] #result
        
#         for i in range(len(freq) - 1, 0, -1): #iterating  from (len(freq) - 1) to 0
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        res = []
        
        #determines frequency of each element
        counts = collections.Counter(nums)
        max_freq = max(counts.values())
        
        buckets = [[] for i in range(max_freq + 1)]
        
        for n, c in counts.items():
            buckets[c].append(n)
            
        for i in range(len(buckets) - 1, 0 , -1):
            for n in buckets[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
            
            