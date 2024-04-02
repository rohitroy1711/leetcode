class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        islands = 0
        visited = set()
        
        
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited.add((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands