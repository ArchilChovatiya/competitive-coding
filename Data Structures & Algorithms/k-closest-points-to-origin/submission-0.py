class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            heapq.heappush(maxHeap,(-math.sqrt(point[0]**2 + point[1]**2),point))
            if len(maxHeap) == k + 1:
                heapq.heappop(maxHeap)
        return [point for (_,point) in maxHeap]