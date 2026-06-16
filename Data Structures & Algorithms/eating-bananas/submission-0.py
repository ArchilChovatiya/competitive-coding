class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        minSp = max(piles)
        while l <= r:
            sp = l + (r-l)//2
            t = 0
            for p in piles:
                t += math.ceil(p/sp)
            if t <= h:
                minSp = min(minSp,sp)
                r = sp - 1
            else:
                l = sp + 1
        return minSp
