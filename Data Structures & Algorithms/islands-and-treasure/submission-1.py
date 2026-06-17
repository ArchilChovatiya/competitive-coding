class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.appendleft((i, j , 0))
        visited = set()
        while q:
            (i , j, dist) = q.pop()
            if i < 0 or j < 0 or i >=len(grid) or j >=len(grid[0]) or (i,j) in visited or grid[i][j]==-1:
                continue
            
            visited.add((i,j))
            grid[i][j] = dist

            q.appendleft((i+1,j, dist+1))
            q.appendleft((i,j+1, dist+1))
            q.appendleft((i-1,j, dist+1))
            q.appendleft((i,j-1, dist+1))
            