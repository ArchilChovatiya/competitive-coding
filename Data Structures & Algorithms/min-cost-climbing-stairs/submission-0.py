class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [ sys.maxsize for i in range(len(cost)+1)]
        res[0] = res[1] = 0
        for i in range(2, len(res)):
            res[i] = min(res[i-1]+cost[i-1],res[i-2]+cost[i-2])
        return res[-1]