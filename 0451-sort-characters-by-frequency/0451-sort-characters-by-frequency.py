class Solution:
    def frequencySort(self, s: str) -> str:
        
        hashmap = Counter(s)
        max_freq = max(hashmap.values())
        
        buckets = [[] for i in range(max_freq + 1)]
        
        for c, n in hashmap.items():
            buckets[n].append(c)
            
            string_builder = []
            
            for i in range(len(buckets) - 1, 0, -1):
                for c in buckets[i]:
                    string_builder.append(c * i)
                    
        return "".join(string_builder)
        
        
        