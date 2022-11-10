class OrderedStream:

    def __init__(self, n: int):
        self.hashmap = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
       
        result = []
        self.hashmap[idKey] = value
        while self.ptr in self.hashmap:
            result.append(self.hashmap[self.ptr])
            del self.hashmap[self.ptr]
            self.ptr += 1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)