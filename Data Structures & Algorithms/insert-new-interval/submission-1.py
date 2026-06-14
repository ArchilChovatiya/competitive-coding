class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
            i+=1 
        
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        return res


            