class Node:
	def __init__(s, key, value):
		s.key = key
		s.value = value
		s.next = None
		s.prev = None
    
class LRUCache:
	def __init__(self, capacity: int):
		self.mru = Node(-1, -1)
		self.lru = Node(-1, -1)
		self.mru.next = self.lru
		self.lru.prev = self.mru
		self.hash = {}
		self.size = capacity

    
	def get(self, key: int) -> int:
		if key not in self.hash:
			return -1
		node = self.hash[key]
		self.delete(node)
		self.insert(node)
		return node.value

	def put(self, key: int, value: int) -> None:
		if key in self.hash:
			node = self.hash[key]
			self.delete(node)
		if self.size == len(self.hash):
			self.delete(self.lru.prev)
		self.insert(Node(key, value))

	def insert(self, node):
		self.mru.next.prev = node
		node.next = self.mru.next
		self.mru.next = node
		node.prev = self.mru
		self.hash[node.key] = node

	def delete(self, node):
		self.hash.pop(node.key)
		node.next.prev = node.prev
		node.prev.next = node.next