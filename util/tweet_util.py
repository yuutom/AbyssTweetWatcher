import tweepy

# Twitterの検索コマンドは以下を参考に
# https://tech-camp.in/note/technology/99382/

class TweetUtilClass:

    # 引数のキーワードでツイートを取得
    def get_tweet(self, api, keyword):
        tweets = api.search_tweets(q="{} min_faves:10 min_retweets:0 exclude:retweets".format(keyword),tweet_mode='extended', lang='ja', count=50)
        return tweets
    
    # カーソルでツイートを取得
    def get_tweet_by_cursor(self, api, s):
        tweets = tweepy.Cursor(api.search_tweets, q = s,       # APIの種類と検索文字列
                               include_entities = True,        # 省略されたリンクを全て取得
                               tweet_mode = 'extended',        # 省略されたツイートを全て取得
                               result_type = "recent",         # 'popular', 'recent', 'mixed'から選択
                               lang = 'ja').items(30)          # 日本のツイートのみ取得
        return tweets

    # タイムラインの内容を取得
    def get_timeline(self, api):
        tweets = api.home_timeline()
        return tweets
