class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = [] # result
        
        def dfs(graph, idx, curr_path, dest):
            for v in graph[idx]: # for every vertex in our graph
                if v == dest: #if our vertex == destination
                    temp = [x for x in curr_path] #create a temp and store the curr_path in it
                    temp.append(v) #append that vertex in it
                    res.append(temp) #and append that temp to result
                else: 
                    curr_path.append(v) #append v to curr_path
                    dfs(graph, v, curr_path, dest) #call dfs on that v
                    curr_path.pop() # i have seen this point, i want to go through another edge
            
        dfs(graph, 0, [0], len(graph) - 1)
        return res
                