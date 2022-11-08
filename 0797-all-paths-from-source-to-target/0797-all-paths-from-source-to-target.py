class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(graph, idx, curr_path, dest):
            for v in graph[idx]:
                if v == dest:
                    temp = [x for x in curr_path]
                    temp.append(v)
                    res.append(temp)
                else:
                    curr_path.append(v)
                    dfs(graph, v, curr_path, dest)
                    curr_path.pop() # i have seen this point, i want to go through another edge
            
        dfs(graph, 0, [0], len(graph) - 1)
        return res
                