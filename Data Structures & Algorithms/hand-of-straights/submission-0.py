class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand  = list(count.keys())
        heapq.heapify(hand)
        while hand:
            while hand and count[hand[0]] == 0:
                heapq.heappop(hand)
            if hand:
                size = 0
                for i in range(hand[0], hand[0]+groupSize):
                    if i in count:
                        size+=1
                        if count[i] == 1:
                            del count[i]
                        else:
                            count[i]-=1
                    else:
                        return False
                if size < groupSize: return False
        return True



