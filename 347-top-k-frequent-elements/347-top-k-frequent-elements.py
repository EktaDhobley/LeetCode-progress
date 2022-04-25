class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {} #Map to map frequencies to elements
        freq = [[] for i in range(len(nums) + 1)] #to store frequency of each value
        
        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0) #counting the numbe rof frequencies
        for n, c in count_map.items(): #mapping frequencies to value
            freq[c].append(n)
            
        res = [] #result
        
        for i in range(len(freq) - 1, 0, -1): #iterating  from (len(freq) - 1) to 0
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res