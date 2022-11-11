# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getCoordinates(self, root, x, y, coordinates):
        if not root:
            return coordinates
        
        coordinates.append([x, y, root.val])
        coordinates = self.getCoordinates(root.left, x - 1, y - 1, coordinates)
        coordinates = self.getCoordinates(root.right, x + 1, y - 1, coordinates)
        
        return coordinates
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #three things to check
        #x coordinate to be sorted in increasng order
        #y in decreasing order
        #and if two values in same col, sort by their value(increasing)
        
        
        if not root:
            return []
        # 0   1   2
        #[x1, y1, val1], [x2, y2, val2] ...
        coordinates = self.getCoordinates(root, 0, 0, [])
        coordinates.sort(key = lambda x: (x[0], -x[1], x[2]))
        
        result = [[coordinates[0][2]]] #new bucket(array/list) for each column
        for i in range(1, len(coordinates)):
            if coordinates[i][0] == coordinates[i - 1][0]: #if in same column
                result[-1].append(coordinates[i][2]) #2 because we want value only
            else:
                result.append([coordinates[i][2]])
        return result
            
            
            
            
            
        