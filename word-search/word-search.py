class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path:
                return False
            
            #path.add((r,c))
            tmp = board[r][c]
            board[r][c] = "#"
            res =  (dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1) or 
                    dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1))
            board[r][c] = tmp
            #path.remove((r,c)) #we dont want to visit this position again, because already explored it and its neighbors
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
    
    #TC = O(n * m * 4^(N)) # n * m = dimensions f=of board
            #where N = len(word) , 4 because we visit in all 4 directions
            
        