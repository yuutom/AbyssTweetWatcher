from tracemalloc import stop
from py import process
from sympy import python
from util.ai_util import AIUtilClass
from util.auth_util import AuthUtilClass
from util.tweet_util import TweetUtilClass
from util.csv_util import CSVUtilClass
from util.common_util import CommonUtilClass
import MeCab
import collections
import re
import os
from collections import defaultdict


def main():

  # クラスオブジェクト取得
  auth_util_class = AuthUtilClass()
  csv_util_class = CSVUtilClass()
  common_util_class = CommonUtilClass()
  tweet_util_class = TweetUtilClass()
  
  # API認証
  api = auth_util_class.get_api()
  
  # CSVファイルから検索用ワードリスト作成
  search_word_list = csv_util_class.get_search_word_list('search_word_list.csv')
  
  # もしツイート収集結果CSVがあれば削除
  if os.path.isfile('tweet_test.csv'):
    os.remove('tweet_test.csv')
      
  # 検索用ワードで繰り返し
  for index, search_word in enumerate(search_word_list):
    
    # 検索用ワードでAPI実行、実行結果を格納
    tweets = tweet_util_class.get_tweet(api, search_word)

    # ツイートオブジェクトの各要素をリスト形式に変換
    tweet_list = common_util_class.tweets_to_list(tweets)
    
    # もしこれが一週目ならCSVファイル作成
    if index == 0:
      csv_util_class.create_csv(tweet_list)
    
    # 二週目以降ならCSVファイルに追記
    else:
      csv_util_class.add_csv(tweet_list)
  
  # ツイートのテキストのみを抽出したリストを作成
  text_list = csv_util_class.make_text_list('tweet_test.csv')
  
  # 頻出単語の抽出、各単語の出現回数のリストのリストを作成
  word_count_result_list = get_word_count_result_list()
  
  # もし単語リストファイルが存在すれば削除
  if os.path.isfile('word_count_result.csv'):
    os.remove('word_count_result.csv')
    
  # 新しい単語リストファイルを作成
  csv_util_class.create_word_count_result_csv(word_count_result_list)

  # もしツイートランキングファイルが存在すれば削除
  if os.path.isfile('tweet_ranking.csv'):
    os.remove('tweet_ranking.csv')
    
  # 新しいランキングファイルを作成
  csv_util_class.create_tweet_ranking_csv()
  
  # htmlリンクファイルが存在すれば削除
  if os.path.isfile('html.csv'):
    os.remove('html.csv')
  
  # スコア上位7のツイートリストを作成
  stop_word_list = csv_util_class.get_stop_word_list('stop_word_list.csv')
  text_score_list = csv_util_class.create_top_7_tweet_list(stop_word_list)
  
  # htmlリンクファイル作成
  # csv_util_class.create_html_csv(api, text_list)
  html_list = []
  for text_score in text_score_list:
      url = text_score[0]
      oembed = api.get_oembed(url)
      html = oembed.get("html")
      html_list.append([html])
  csv_util_class.create_html_csv(html_list)
  


def get_wakati_list():
  """分かちテキストリストの作成（現在は未使用）

  Returns:
      list: 分かちテキストリスト
  """
  csv_util_class = CSVUtilClass()
  text_list = csv_util_class.make_text_list('tweet_test.csv')
  mecab = MeCab.Tagger("-Owakati")
  words_list = []
  for text in text_list:
    node = mecab.parseToNode(text)
    words=[]
    while node:
        part_of_speech = node.feature.split(",")[0]
        if part_of_speech == "名詞":
            origin = node.surface
            words.append(origin)
        node = node.next
    words_list.append(words)
  return words_list


def get_word_count_result_list():
  """[キーワード, 出現回数]を取得
     [["python", 30], ["プログラミング", 10], ・・・]（リスト順は出現回数降順）

  Returns:
      list: [キーワード, 出現回数]のリスト
  """
  # クラスオブジェクト取得
  csv_util_class = CSVUtilClass()
  ai_util_class = AIUtilClass()
  
  # 訓練用テキストリストを取得
  text_train = csv_util_class.get_text_train()
  
  # 訓練用ラベルリストを取得
  y_train = csv_util_class.get_y_train()
  
  # 機械学習モデルを作成
  logreg, vect = ai_util_class.get_logreg_model(text_train, y_train)
  
  text_list = csv_util_class.make_text_list('tweet_test.csv')
  stop_word_list = csv_util_class.get_stop_word_list('stop_word_list.csv')
  mecab = MeCab.Tagger("-Owakati")
  preprocessed_text_list = []
  for text in text_list:
    preprocessed_text_before = ai_util_class.preprocess(text)
    preprocessed_text = vect.transform([preprocessed_text_before])
    if logreg.predict(preprocessed_text.toarray()) == '1':
      preprocessed_text_list.append(preprocessed_text_before)

  vector, word_vector = ai_util_class.get_count_vectorizer(preprocessed_text_list)
  
  number_of_appearances_list = []
  count_list = [0]*len(vector.get_feature_names())
  for counts in word_vector:
    for index, num in enumerate(counts):
      count_list[index] = count_list[index] + num
  for word, count in zip(vector.get_feature_names(), count_list):
    number_of_appearances_list.append([word.replace(' ',''), count])
    number_of_appearances_list.sort(key=lambda x: x[1], reverse=True)
  return number_of_appearances_list
  
  

  

if __name__ == "__main__":
  main()