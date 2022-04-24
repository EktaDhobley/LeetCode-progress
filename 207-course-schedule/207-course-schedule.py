class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) }
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
            #visit_set will have all courses along the DFS path
        visit_set = set()
            
        def dfs(crs):
            if crs in visit_set: #to check if its a loop
                return False
            if preMap[crs] == []: #if no prereq return true, we can take that course
                return True
                
            visit_set.add(crs)
                
            for pre in preMap[crs]:
                if not dfs(pre): return False
                    
            visit_set.remove(crs) #because we can take that course
            preMap[crs] = [] #if this particular is a prereq for some other course, we can directly return true, instead of doing the whole process again (line 14)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True    