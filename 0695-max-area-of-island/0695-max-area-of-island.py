class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        #all_areas = []
        def bfs(i,j) -> int:
            q = collections.deque() 
            q.append((i,j))
            visit.add((i,j))
            temp = 1
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row+dr
                    c = col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        temp +=1
                        q.append((r,c))
                        visit.add((r,c))
            #all_areas.append(temp)
            return temp
                    
                
            
        
        area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    area = max(area,bfs(i,j))
                    
        
        #print(all_areas)
        return area