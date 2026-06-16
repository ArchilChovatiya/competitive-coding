from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap =[-count for count in counts.values()]
        heapq.heapify(maxHeap)
        buffer =  deque()
        time = 0
        while buffer or maxHeap:
            if buffer and buffer[-1][1] < time:
                heapq.heappush(maxHeap, buffer.pop()[0])
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                curr+=1
                if curr !=0:
                    buffer.appendleft((curr, time + n))
            time+=1
        return time
             

