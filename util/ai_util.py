from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from util.csv_util import CSVUtilClass
import MeCab
import numpy as np
import re

class AIUtilClass:
    
    def get_count_vectorizer(self, preprocessed_text_list):
        vector = CountVectorizer(min_df=4, ngram_range=(1, 2))
        result = vector.fit_transform(preprocessed_text_list)
        word_vector = result.toarray()
        return vector, word_vector
    
    def get_logreg_model(self, text_train, y_train):
        vect = CountVectorizer().fit(text_train)
        X_train = vect.transform(text_train)
        logreg = LogisticRegression().fit(X_train, y_train)
        return logreg, vect
    
    def preprocess(self, text):
        csv_util_class = CSVUtilClass()
        stop_word_list = csv_util_class.get_stop_word_list('stop_word_list.csv')
        mecab = MeCab.Tagger("-Owakati")
        X_train = []
        words = []
        text = re.sub(r"#(\w+)", "", text)
        text = re.sub(r"＃(\w+)", "", text)
        text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
        text = text.replace('\n','')
        node = mecab.parseToNode(text)
        while node:
            part_of_speech = node.feature.split(",")[0]
            if part_of_speech == "名詞":
                origin = node.surface
                if origin not in stop_word_list:
                    words.append(origin)
            node = node.next
        preprocessed_text = " ".join(words)
        
        return preprocessed_text