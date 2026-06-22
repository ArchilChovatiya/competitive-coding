class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        last = 0
        count = 0
        for i, c in enumerate(s):
          count+=1
          last = max(lastIndex[c], last)
          if i == last:
            res.append(count)
            count = 0
        return res



                