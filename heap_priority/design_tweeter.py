"""
Design a simplified Twitter where users can post
tweets and retrieve the 10 most recent tweets in
their news feed (their own and those they follow).

Example:
  postTweet(1,5); getNewsFeed(1)->[5]
  follow(1,2); postTweet(2,6); getNewsFeed(1)->[6,5]

Constraints:
  A min-heap merges the most recent tweets across followees.
"""

from collections import defaultdict
from typing import List
import heapq


class Twitter:
    def __init__(self):
        # Decreasing counter makes newest tweets sort first.
        self.count = 0
        # Maps userId -> list of [count, tweetId].
        self.tweet_map = defaultdict(list)
        # Maps userId -> set of followeeIds.
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        min_heap = []

        # Users always see their own tweets.
        self.follow_map[userId].add(userId)
        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                count, tweet_id = self.tweet_map[followee_id][index]
                # Heap entry enables fetching the next tweet later.
                heapq.heappush(
                    min_heap,
                    [count, tweet_id, followee_id, index - 1],
                )

        while min_heap and len(result) < 10:
            count, tweet_id, followee_id, index = heapq.heappop(
                min_heap
            )
            result.append(tweet_id)
            # Add the next older tweet from the same followee.
            if index >= 0:
                count, tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(
                    min_heap,
                    [count, tweet_id, followee_id, index - 1],
                )
        return result

    def follow(
        self, follower_id: int, followee_id: int
    ) -> None:
        self.follow_map[follower_id].add(followee_id)

    def unfollow(
        self, follower_id: int, followee_id: int
    ) -> None:
        if followee_id in self.follow_map[follower_id]:
            self.follow_map[follower_id].remove(followee_id)
