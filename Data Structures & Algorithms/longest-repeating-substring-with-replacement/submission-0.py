class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = r = 0
        maxLength = 0
        while r < len(s):
            counts[s[r]] = counts.get(s[r],0) + 1
            while r - l + 1 - max(counts.values()) > k:
                counts[s[l]]-=1
                l+=1
            maxLength = max(maxLength, r-l+1)
            
            r+=1
        return maxLength