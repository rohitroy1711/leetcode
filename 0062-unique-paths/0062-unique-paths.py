class Solution(object):
    def uniquePaths(self, m, n):
        N = m+n-2
        R = m-1
        num = 1
        den = 1
        for i in range(0,R):
            num = (N-i)*num
            den = (R-i)*den
        ans = num//den
        return ans
        
#         We can also solve this problem using Permutations and combinations
        
        
#         The below is the code using dynamic progrramming
#         memo = {}
#         def paths(i,j):
#             if i == m-1 and j == n-1:
#                 return 1
#             if i > m-1 or j > n-1:
#                 return 0
#             if (i,j) in memo:
#                 return memo[(i,j)]
#             else:
#                 memo[(i,j)] =  paths(i+1,j)+paths(i,j+1)
#                 return memo[(i,j)]
#         return paths(0,0)
        
        