# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {} #map key to nodes #cache is hashmap
        
#         self.left, self.right = Node(0,0), Node(0,0) 
#         #initially we want left and right nodes to be connected to each other, because when we add any nodes, we want those nodes to be added between them
#         self.left.next, self.right.prev = self.right, self.left #left = LRU, right = most recent used (MRU)

# #remove node from linked list
# def remove(self, node):
#     prev, nxt = node.prev, node.next # 
#     prev.next, nxt.prev = nxt, prev
    
# #insert node at right    
# def insert(self, node):
#     prev, nxt = self.right.prev, self.right
#     prev.next = nxt.prev = node
#     node.next, node.prev = nxt, prev
        
# #everytime we use a get functiomn on any node it becomes MRU
#     def get(self, key: int) -> int:
#         #self.cache[key] is a node since each key is mapped to a node, therefore we do '.val'
#         if key in self.cache:
#             self.remove(self.cache[key]) #MRU
#             self.insert(self.cache[key]) #insert at right
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key]) #inserted at right since its a new node
        
#         if len(self.cache) > self.cap:
#             #remove from Linked List and delete LRU from hashmap(cache)
#             lru = self.left.next
#             self.remove(lru) #remove from LL
#             del self.cache[lru.key] #delete key from HashMap
            

# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]