from sklearn import preprocessing
from sympy import python
from util.auth_util import AuthUtilClass
from util.tweet_util import TweetUtilClass
from util.csv_util import CSVUtilClass
from util.common_util import CommonUtilClass
from util.ai_util import AIUtilClass
import MeCab
import collections
import re
import csv

def main():
  
  # csv_util_class = CSVUtilClass()
  # stop_word_list = csv_util_class.get_stop_word_list('stop_word_list.csv')
  # mecab = MeCab.Tagger("-Owakati")
  # X_train_list = []
  # for text in X_train:
  #   text = re.sub(r"#(\w+)", "", text)
  #   text = re.sub(r"＃(\w+)", "", text)
  #   text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
  #   text = text.replace('\n','')
  #   words=[]
  #   node = mecab.parseToNode(text)
  #   while node:
  #     part_of_speech = node.feature.split(",")[0]
  #     if part_of_speech == "名詞":
  #       origin = node.surface
  #       if origin not in stop_word_list:
  #         words.append(origin)
  #     node = node.next
  #   preprocessed_text = " ".join(words)
  #   X_train_list.append([preprocessed_text])
  # with open('train_text.csv', 'w', newline='',encoding='utf_8_sig') as f:
  #   writer = csv.writer(f, lineterminator='\n')
  #   writer.writerows(X_train_list)

  csv_util_class = CSVUtilClass()
  # ai_utl_class = AIUtilClass()
  # text_train = csv_util_class.get_text_train()
  # y_train = csv_util_class.get_y_train()
  
  # test = "今日は結合確認と不具合修正でおわり〜。curlでダウンロードAPI実行したら長々と文字だけが返ってきてたけど-O オプション付けるだけでよかったのね。リクエスト情報をcurl用に変換してくれるツールないかな🤔今日も一日お疲れ様でした❗️#駆け出しエンジニアと繋がりたい#プログラミング初心者"
  # text = ai_utl_class.preprocess(test)  
  
  # logreg, preprocessed_text = ai_utl_class.get_logreg_model(text_train, y_train, text)
  # print(logreg.predict(preprocessed_text.toarray()))
  csv_util_class.create_tweet_ranking_csv()


if __name__ == "__main__":
  main()









