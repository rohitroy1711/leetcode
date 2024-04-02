class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        areas = []
        islands =0
        
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            temp = 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row+dr
                    c = col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        temp = temp+1
                        q.append((r,c))
                        visited.add((r,c))
            areas.append(temp)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        if not areas:
            return 0
        return max(areas)