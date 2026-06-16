class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def dfs(i , j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if j >=len(s):
                return False

            if (i,j+1) not in memo:
                memo[(i,j+1)] = dfs(i, j+1)

            if s[i:j+1] in wordDict:
                if j==len(s)-1:
                    memo[(i,j)]=True
                    return memo[(i,j)]

                if (j+1,j+1) not in memo:
                    memo[j+1,j+1] = dfs(j+1,j+1)
                return memo[j+1,j+1] or memo[(i,j+1)]
            return memo[(i,j+1)]
        return dfs(0,0)

            