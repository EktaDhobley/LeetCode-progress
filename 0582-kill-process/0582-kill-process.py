class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        graph = defaultdict(list)
        
        for parent,child in zip(ppid, pid):
            graph[parent].append(child)
        
        queue = deque([kill])
        res = []
        while queue:
            
            killed = queue.popleft()
            
            res.append(killed)
            
            if killed in graph:
                queue.extend(graph[killed])
        return res
            
        