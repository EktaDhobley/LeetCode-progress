#APPROACH 1 - Using hashmap and comparator O(NlogN)
# class Solution:
#     def frequencySort(self, s: str) -> str:
        
#         #count occurences
#         counts = collections.Counter(s)
        
#         #building the string builder
#         string_builder = []
#         #most_common() is used to produce a sequence of the n most frequently encountered input values and their respective counts ie it sorts
#         #[('a', 15), ('g', 10), ('y', 10), ('b', 8), ('d', 5)] = counts.most_common()
#         for letter, freq in counts.most_common():
#             string_builder.append(letter * freq)
#         return "".join(string_builder)

#APPROACH 2 - Using HashMap and Bucket Sort O(N)

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        
        #determine freq of each character
        counts = collections.Counter(s)
        max_freq = max(counts.values())
        
        #Bucket sort the characters by frequency
        buckets = [[] for i in range(max_freq+1)] #har ek ke liye ek bucket banega coz of for i in range
        
        for c, i in counts.most_common(): #or use counts.items()
            buckets[i].append(c) #jitna count hai uss hisaab se char insert karo bucket mein
            
            #building the string builder
            string_builder = []
            for i in range(len(buckets) - 1, 0 , -1):
                for c in buckets[i]:
                    string_builder.append(c * i)
                    
        return "".join(string_builder)