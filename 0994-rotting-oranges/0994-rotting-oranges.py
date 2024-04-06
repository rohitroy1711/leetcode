# [2,1,1]
# [0,1,1]
# [1,0,1]
# try to make all the ones into 2's in the matrix
# if any 1 is in the matrix then we can return -1
# if there is no 1 in the matrix we can return the bfs steps that wld be the minimum time taken to damage all the fruits.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        visited = set()
        time = 0
        freshoranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    #time =-1
                if grid[r][c] == 1:
                    freshoranges+=1
        direct = [[0,1],[1,0],[0,-1],[-1,0]]
        while q and freshoranges >0:
            for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in direct:
                        row = r+dr
                        col = c+dc
                        if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                            grid[row][col] = 2
                            freshoranges -=1
                            q.append((row,col))
                  
            time+=1
        
        return time if freshoranges == 0 else -1