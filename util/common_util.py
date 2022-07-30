from sklearn import preprocessing
import re


class CommonUtilClass:

    # ツイートオブジェクトをリストに格納
    def tweets_to_list(self, tweets):
        tweet_list = []
        for tweet in tweets:
            if tweet.user.followers_count < 1000:
                # テキストからURLとハッシュタグを削除
                # text = tweet.full_text
                # text = re.sub(r"#(\w+)", "", text)
                # text = re.sub(r"＃(\w+)", "", text)
                # text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
                # text = text.replace('\n','')
                # URL作成
                tweet_id = tweet.id
                screen_id = tweet.user.screen_name
                # url = "Twitter.com/{}/status/{}".format(screen_id,tweet_id)
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