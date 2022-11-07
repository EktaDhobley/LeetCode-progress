class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
       #define an array 
        triangle = []
        
        for r in range(numRows): #for loop for adding rows to the final triangle (0,1,2,3,4)
            row = [None for i in range(r + 1)] #intiating each row with None, notice the no. of elements in the row
            row[0], row[-1] = 1, 1 #first and last = 1 always
            
            for j in range(1, len(row) - 1): #nested for loop to fill up each row
                row[j] = triangle[r - 1][j - 1] + triangle[r - 1][j] #as seen in question animation, each element is the sum of the elements directly above it
            triangle.append(row) #After filling up the row - append it to the main traingle
        return triangle
                