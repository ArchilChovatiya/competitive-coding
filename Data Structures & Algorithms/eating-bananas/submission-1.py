class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        minSp = max(piles)
        while l <= r:
            m = l + (r-l)//2
            t = 0
            for p in piles:
                t += math.ceil(p/m)
            if t <= h:
                minSp = min(minSp,m)
                r = m - 1
            else:
                l = m + 1
        return minSp
