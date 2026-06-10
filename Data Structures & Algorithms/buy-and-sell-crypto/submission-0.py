class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100
        maxProf = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProf = max(maxProf, price - minPrice)
        return maxProf