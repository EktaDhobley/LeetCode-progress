class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nIslands = nIslands + self.dfs(grid, i, j)
        return nIslands
    def dfs(self, grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0 or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        return 1
        
        
        
#         nIslands = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     nIslands = nIslands + self.dfs(grid, i, j)
#         return nIslands
    
    
#     def dfs(self, grid, i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
#             return 0
        
#         grid[i][j] = '0'
#         self.dfs(grid, i , j+1)
#         self.dfs(grid, i, j -1)
#         self.dfs(grid, i + 1, j)
#         self.dfs(grid, i - 1, j)
#         return 1