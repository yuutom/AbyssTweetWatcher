import csv

class CSVUtilClass:

    # CSVに出力(新規作成)
    def create_csv(self, tweet_list):
        with open('tweet_test.csv', 'w', newline='',encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(tweet_list)

    # CSVに出力(追記)
    def add_csv(self, tweet_list):
        with open('tweet_test.csv', 'a', newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(tweet_list)

  # CSVに出力(検索ワードリスト新規作成)
    def create_search_word_csv(self):
        with open('search_word_list.csv', 'w', newline='',encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            search_word_list = [["python"], ["エンジニア"], ["機械学習"], ["ディープラーニング"], ["API"], ["データサイエンティスト"], ["データサイエンス"], ["人工知能"], ["AI"]]
            writer.writerows(search_word_list)
            
  # CSVに出力(検索ワードリスト追記)
    def add_search_word_csv(self, search_word_list):
        with open('tweet_test.csv', 'a', newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(search_word_list)
            
  # CSVに出力(ストップワードリスト新規作成)
    def create_stop_word_csv(self):
        with open('stop_word_list.csv', 'w', newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            stop_word_list = [["今日"], ["機械"], ["学習"], ["こと"], ["自分"], ["データ"], ["サイエンティスト"], ["初心"], ["co"]]
            writer.writerows(stop_word_list)
            
  # CSVに出力(ストップワードリスト追記)
    def add_search_word_csv(self, stop_word_list):
        with open('stop_word_list.csv', 'a', newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(stop_word_list)
            
    # CSVに出力(新規作成)
    def create_word_count_result_csv(self, word_count_result):
        with open('word_count_result.csv', 'w', newline='',encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(word_count_result)

    # CSVを読み込み
    def read_csv(self, path):
        with open(path, encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                print(row)
                
    # 分析用テキスト作成
    def make_text(self, path):
        text = ""
        with open(path, encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                text = text + row[3]
        return text
    
    # 分析用テキストリスト作成
    def make_text_list(self, path):
        text_list = []
        with open(path, encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                text_list.append(row[3])
        return text_list
    
    # 検索ワードリスト取得
    def get_search_word_list(self, path):
        search_word_list = []
        with open(path, encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                search_word_list.append(row[0])
        return search_word_list

    # ストップワードリスト取得
    def get_stop_word_list(self, path):
        stop_word_list = []
        with open(path, encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                stop_word_list.append(row[0])
        return stop_word_list
    
    # text_train取得
    def get_text_train(self):
        text_train = []
        with open('text_train.csv', encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                text_train.append(row[0])
        return text_train
    
    # y_train取得
    def get_y_train(self):
        y_train = []
        with open('train_data.csv', encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                y_train.append(row[9])
        return y_train
    
    # tweetランキングファイル作成
    def create_tweet_ranking_csv(self):
        text_score_list = []
        with open('tweet_test.csv', encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                text_score_list.append([row[8], row[9], row[3]])
        text_score_list.sort(key=lambda x: x[1], reverse=True)
        text_score_list = text_score_list[:10]
        with open('tweet_ranking.csv', 'w', newline='',encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(text_score_list)
    
    # 棒グラフ作成用リスト作成
    def create_bar_chart_elemet_list(self, stop_word_list):
        word_list = []
        count_list = []
        with open('word_count_result.csv', encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                if row[0] not in stop_word_list:
                    if not row[0].isdigit():
                        word_list.append(row[0])
                        count_list.append(int(row[1]))
        word_list = word_list[:40]
        count_list = count_list[:40]
        return word_list, count_list
    
    # スコア上位7のツイートリストを作成
    def create_top_7_tweet_list(self, stop_word_list):
        text_score_list = []
        with open('tweet_ranking.csv', encoding='utf_8_sig', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                text_score_list.append([row[0], row[1]])
        text_score_list = text_score_list[:7]
        return text_score_list
    
    # htmlリンクファイル作成
    def create_html_csv(self, html_list):
        # html_list = []
        # for text_score in text_score_list:
        #     url = text_score[0]
        #     oembed = api.get_oembed(url)
        #     html = oembed.get("html")
        #     html_list.append([html])
        with open('html.csv', 'w', newline='',encoding='utf_8_sig') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(html_list)