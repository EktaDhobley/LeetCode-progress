
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         res = [] #result array
        
#         #determines frequency of each element
#         counts = collections.Counter(nums) #hashmap for getting frequency of each element
#         max_freq = max(counts.values())
        
#         buckets = [[] for i in range(max_freq + 1)] # bucket with frequencies
        
#         for n, c in counts.items(): #add numbers to respective buckets
#             buckets[c].append(n)
            
#         for i in range(len(buckets) - 1, 0 , -1): #iterate thriugh buckets from end (to get maximum)
#             for n in buckets[i]:
#                 res.append(n)
                
#                 if len(res) == k:
#                     return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        h = [] #result heap
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
                
        for key, count in freq.items():
            if len(h) < k:
                heappush(h, [count, key])
            else:
                heappushpop(h, [count, key])
        return [key for count, key in h]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            