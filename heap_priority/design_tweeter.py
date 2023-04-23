"""
strategy to solve the problem
"""
from collections import defaultdict
from typing import List
import heapq
class Twitter:
    def __init__(self):
        self.count = 0 #how new is the tweet
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        #using hash set because add and remove will take O(1)
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] #list of tweet id
        minHeap = []

        self.followMap[userId].add(userId)
        #put all newest tweet from followee
        for followeeId in self.followMap[userId]: #get follwee of a follower
            if followeeId in self.tweetMap: #check followee have in tweetMap
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                #[count, tweetId, followeeId, index-1]. count for heap ranking, tweetId for res, followeeId and index-1 to get next count and tweetId for next iteration
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        #get newest tweet from all followee
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            #pop one tweet from followee and then add new one
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
