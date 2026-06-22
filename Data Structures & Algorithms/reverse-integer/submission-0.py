class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        res = 0
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        if negative:
            res = -res
            
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res