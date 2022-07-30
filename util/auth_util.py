import tweepy
from const.auth_const import AuthConstClass

class AuthUtilClass:

    def get_api(self):
        const = AuthConstClass()
        API_KEY = const.API_KEY
        API_KEY_SECRET = const.API_KEY_SECRET
        ACCESS_TOKEN = const.ACCESS_TOKEN
        ACCESS_TOKEN_SECRET = const.ACCESS_TOKEN_SECRET
        
        auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit = True) # API利用制限にかかった場合、解除まで待機する
        
        return api