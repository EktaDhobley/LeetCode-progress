class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            
            while res != par[res]: #while it is not a parent of itself
                par[res] = par[par[res]] #path compression
                res = par[res]
            return res
        
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return 0
                
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
                
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
                
            return 1
        
        res = n
        for n1, n2 in edges:
            res = res - union(n1,n2)
            
        return res    
                