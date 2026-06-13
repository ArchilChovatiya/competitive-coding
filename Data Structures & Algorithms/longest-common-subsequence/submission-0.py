class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n , m = len(text1), len(text2)

        res = [[0]* (m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    res[i][j] = res[i-1][j-1]+1
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
        return res[-2][-2]