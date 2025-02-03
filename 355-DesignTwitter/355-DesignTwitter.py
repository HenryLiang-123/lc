from collections import deque
class Twitter:

    def __init__(self):
        self.user_to_tweet = defaultdict(deque)
        self.user_to_following = defaultdict(set)
        self.tweet_to_time = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # post to self
        self.user_to_tweet[userId].appendleft(tweetId)
        if len(self.user_to_tweet[userId]) > 10:
            expired_tweet = self.user_to_tweet[userId].pop()
            del self.tweet_to_time[expired_tweet]

        # record time and sort
        self.tweet_to_time[tweetId] = self.time
        # self.tweet_to_time = {k: self.tweet_to_time[k] for k in sorted(self.tweet_to_time)}
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_self = list(self.user_to_tweet[userId])
        followers = list(self.user_to_following[userId])
        news_follower = []
        for i in range(len(followers)):
            news_of_follower = self.user_to_tweet[followers[i]]
            news_follower.extend(news_of_follower)
        
        n_self = len(news_self)
        n_follower = len(news_follower)
        p1, p2 = 0,0
        result = []
        news_to_time_self = sorted([(self.tweet_to_time[i], i) for i in news_self], reverse=True)
        news_to_time_follower = sorted([(self.tweet_to_time[i], i) for i in news_follower], reverse=True)
        print(news_self, news_follower)
        print([self.tweet_to_time[i] for i in news_self], [self.tweet_to_time[i] for i in news_follower])
        while p1 < n_self and p2 < n_follower:
            tweetId_self = news_to_time_self[p1][1]
            tweetId_follower = news_to_time_follower[p2][1]

            if news_to_time_self[p1][0] > news_to_time_follower[p2][0]:
                result.append(tweetId_self)
                p1 += 1
            else:
                result.append(tweetId_follower)
                p2 += 1
        
        if p1 < n_self and len(result) < 10:
            while len(result) < 10 and p1 < n_self:
                tweetId_self = news_to_time_self[p1][1]
                result.append(tweetId_self)
                p1 += 1
        else:
            while len(result) < 10 and p2 < n_follower:
                tweetId_follower = news_to_time_follower[p2][1]
                result.append(tweetId_follower)
                p2 += 1

        # tweetId_self = news_self[i]
        # tweetId_follower = news_follower[i]


        return result[:10]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_to_following[followerId]:
            self.user_to_following[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)