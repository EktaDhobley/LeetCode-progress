class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
       #define an array 
        triangle = []
        
        for r in range(numRows): #eg numRows = 5
            row = [None for i in range(r + 1)] #r + 1 = 1,2..
            row[0], row[-1] = 1, 1 #first and last = 1 always
            
            for j in range(1, len(row) - 1):
                row[j] = triangle[r - 1][j - 1] + triangle[r - 1][j]
            triangle.append(row)
        return triangle
                