class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * (n+1) for _ in range(m+1)]
        for j in range(m):
            for i in range(n):
                if i == 0 and j==0: 
                    res[j][i] = 1
                    continue
                res[j][i] = res[j-1][i] + res[j][i-1]
        return res[-2][-2]