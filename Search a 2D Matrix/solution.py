class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oneLine = self.searchVertical(matrix, target)
        print(oneLine)
        if oneLine is None:
            return False
        return self.searchHorizon(oneLine, target)
        
    def searchHorizon(self, line, target):
        if len(line) == 0:
            return False
        elif len(line) == 1:
            return line[0] == target
        
        mid = len(line) // 2
        
        if target < line[mid]:
            return self.searchHorizon(line[:mid], target)
        elif target > line[mid]:
            return self.searchHorizon(line[mid:], target)
        else:
            return True
    
    def searchVertical(self, matrix, target):

        if len(matrix) == 1:
            return matrix[0]
        elif len(matrix) == 0:
            return None
    
        mid = len(matrix) // 2
        
        if target < matrix[mid][0]:
            return self.searchVertical(matrix[:mid], target)
        else:
            return self.searchVertical(matrix[mid:], target)
        
