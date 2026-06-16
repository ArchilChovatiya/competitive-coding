class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def helper(start):
            if start in memo:
                return memo[start]
            if start== len(s):
                return True
            for i in range(start,len(s)):
                if s[start:i+1] in wordDict:
                    memo[i+1] = helper(i+1)
                    if memo[i+1]: 
                        return True
            return False
        return helper(0)
            
            