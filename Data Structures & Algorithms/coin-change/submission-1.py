class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount+1)
        dp[0]=0
        coins.sort()
        for a in range(1,amount+1):
            for c in coins:
                if c > a: break
                dp[a] = min(dp[a],dp[a-c]+1)
        return dp[-1] if dp[-1]!=sys.maxsize else -1



