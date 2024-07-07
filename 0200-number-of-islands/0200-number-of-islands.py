class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        islands = 0
        
        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            
            while q:
                row,col = q.popleft()
                directions = [[1,0],[0,1],[0,-1],[-1,0]]
                for dr,dc in directions:
                    nr = row+dr
                    nc = col+dc
                    
                    if (nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] =="1" and (i,j) not in visit:
                    bfs(i,j)
                    islands+=1
        
        return islands