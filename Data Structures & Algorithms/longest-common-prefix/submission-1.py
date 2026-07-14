class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0  
        res = []
        first = strs[0]
        while True:
            for s in strs:
                if i >= len(s) or s[i]!=first[i]:
                    return "".join(res)
            res.append(first[i])
            i+=1
        return "".join(res)
            
                
