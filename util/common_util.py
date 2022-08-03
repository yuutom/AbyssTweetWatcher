from sklearn import preprocessing
import re


class CommonUtilClass:

    # ツイートオブジェクトをリストに格納
    def tweets_to_list(self, tweets):
        tweet_list = []
        for tweet in tweets:
            if tweet.user.followers_count < 2000:
                text = tweet.full_text
                if "今日の積み上げ" not in text:
                    tweet_id = tweet.id
                    screen_id = tweet.user.screen_name
                    url = "https://twitter.com/{}/status/{}".format(screen_id,tweet_id)
                    score = int(tweet.favorite_count) + int(tweet.retweet_count)
                    tweet_list.append([tweet.id,
                                    tweet.user.screen_name,
                                    tweet.created_at,
                                    tweet.full_text.replace('\n',''),
                                    tweet.favorite_count,
                                    tweet.retweet_count,
                                    tweet.user.followers_count,
                                    tweet.user.friends_count,
                                    url,
                                    score
                                    ])
        
        return tweet_list