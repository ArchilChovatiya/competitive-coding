class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp,tweetId))
        self.timestamp+=1
        if userId not in self.followers:
            self.followers[userId].add(userId)        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        for followeeId in self.followers[userId]:
            for (timestamp, tweetId) in self.posts[followeeId]:
                heapq.heappush(minHeap, (timestamp,tweetId))
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        while minHeap:
            res.append(heapq.heappop(minHeap))
        res.reverse()
        return [x[1] for x in res]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId].add(followerId)             
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId] and followerId!=followeeId:
            self.followers[followerId].remove(followeeId)
