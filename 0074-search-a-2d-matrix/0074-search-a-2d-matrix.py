class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1
        ans = False
        while row<len(matrix):
            if target <= matrix[row][col]:
                l=0
                r=len(matrix[0])-1
                
                while l<=r:
                    m = l+(r-l)//2
                    if target < matrix[row][m]:
                        r = m-1
                    elif target > matrix[row][m]:
                        l = m+1
                    else:
                        return True
                        
            row+=1
            
        return ans
                
                
            