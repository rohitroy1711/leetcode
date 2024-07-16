class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        q.append((0,0,1))
        visit.add((0,0))
        directions = [[0,1],[1,0],[0,-1],[-1,0]
                     ,[1,1],[1,-1],[-1,-1],[-1,1]]
        leng = 1
        while q:
            r,c,leng = q.popleft()
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 1:
                continue
            if r == rows-1 and c == cols-1:
                return leng
            for dr,dc in directions:
                row = r+dr
                col = c+dc
                if (row,col) not in visit:
                    q.append((row,col,leng+1))
                    visit.add((row,col))
        return -1