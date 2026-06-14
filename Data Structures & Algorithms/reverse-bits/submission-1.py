class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for _ in range(32):
            bits.append(n & 1)
            n = n >> 1
        res = 0
        bits.reverse()
        print(bits)
        while bits:
            res = res << 1
            res = res | bits.pop()
        return  res 
