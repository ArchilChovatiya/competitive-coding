class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l  = r = 0
        length = maxLength = 0
        visited = set()
        while r < len(s):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1 ; length-=1
            visited.add(s[r])
            r+=1 ; length+=1
            maxLength = max(length, maxLength)
        return maxLength