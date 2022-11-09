class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res: #not present already
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res  

    def remove(self, val: int) -> bool:
        
        res = val in self.numMap
        if res:
            idx = self.numMap[val] #index of element to be removed
            lastVal = self.numList[-1] #get last ele of list
            self.numList[idx] = lastVal #put the last ele val on the idx which needs to be removed 
            self.numList.pop() #pop the last ele from list
            self.numMap[lastVal] = idx #now make the lastVal's origiinal pointer to map at idx
            del self.numMap[val] #now delete the required value from the map
        return res 
    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()