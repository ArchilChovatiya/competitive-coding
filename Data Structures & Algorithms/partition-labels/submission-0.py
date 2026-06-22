class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        last = 0
        count = 0
        for i, c in enumerate(s):
            if i <= last:
                count+=1
                last = max(last,lastIndex[c])
            else:
                res.append(count)
                count = 1
                last = lastIndex[c]
        res.append(count)
        return res



                