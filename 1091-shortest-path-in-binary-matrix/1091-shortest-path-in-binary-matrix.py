class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = collections.deque()
        q.append((0,0))
        visited.add((0,0))
        length = 0
        
        direct = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        while q:
            for i in range(len(q)):
                row,col = q.popleft()
                if row == rows-1 and col == cols-1:
                    return length+1
                for dr,dc in direct:
                    nr = row+dr
                    nc = col+dc
                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == 1 or (nr,nc) in visited:
                        continue
                    q.append((nr,nc))
                    visited.add((nr,nc))
            length+=1
        return -1
                
        
        