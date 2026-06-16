class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 , n2 = len(s1), len(s2)
        if n1 > n2: return False
        c1 , c2 = [0]*26, [0]*26
        for i in range(len(s1)):
            c1[ord(s1[i])-ord('a')]+=1
            c2[ord(s2[i])-ord('a')]+=1
        c1 = tuple(c1)
        if c1 == tuple(c2): return True
        i = 0
        for j in range(n1, n2):
            c2[ord(s2[j])-ord('a')] +=1
            c2[ord(s2[i])-ord('a')] -=1
            i+=1
            if c1 == tuple(c2):
                return True
        return False


        