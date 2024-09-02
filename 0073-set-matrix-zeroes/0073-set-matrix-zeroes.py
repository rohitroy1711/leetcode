class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = [0]*len(matrix)
        c = [0] *len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r[i] = 1
                    c[j] = 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r[i] or c[j] == 1:
                    matrix[i][j] = 0
        