class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q =deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.appendleft((i, j, 0))
        visited = set()
        maxTime = 0
        while q:
            (i, j, time) = q.pop()
            if i<0 or j<0 or i>=len(grid) or j >=len(grid[0]) or grid[i][j]==0 or (i,j) in visited:
                continue
            
            visited.add((i,j))
            grid[i][j] = 2
            maxTime = max(maxTime,time)
            
            q.appendleft((i, j+1, time+1))
            q.appendleft((i+1, j, time+1))
            q.appendleft((i, j-1, time+1))
            q.appendleft((i-1, j, time+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return maxTime
             