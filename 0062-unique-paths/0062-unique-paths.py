class Solution(object):
    def uniquePaths(self, m, n):
        memo = {}
        def paths(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i > m-1 or j > n-1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            else:
                memo[(i,j)] =  paths(i+1,j)+paths(i,j+1)
                return memo[(i,j)]
        return paths(0,0)
        
        