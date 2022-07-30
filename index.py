import streamlit as st
import streamlit.components.v1 as stc
import numpy as np
import pandas as pd
from util.csv_util import CSVUtilClass
from util.auth_util import AuthUtilClass
import csv
import re
import json

col1, col2 = st.columns(2)

csv_util_class = CSVUtilClass()
stop_word_list = csv_util_class.get_stop_word_list('stop_word_list.csv')
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

df = pd.DataFrame({
    'Frequent words': word_list,
    'Occurrences': count_list
})
with col1:
    st.subheader('今日のトレンドワード')
    st.dataframe(df, width=1000, height=1450)


auth_util_class = AuthUtilClass()
# t = auth_util_class.get_api_by_python_twitter()
t = auth_util_class.get_api()
text_score_list = []
with open('tweet_ranking.csv', encoding='utf_8_sig', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        text_score_list.append([row[0], row[1]])
text_score_list = text_score_list[:7]

with col2:
    st.subheader('今日の人気ツイート')
    for text_score in text_score_list:
        url = text_score[0]
        oembed = t.get_oembed(url)
        html = oembed.get("html")
        stc.html(html)
        # url_re = re.search(re.compile(r'<a href=\"(https://t.co/[A-Za-z0-9]+)\">'), html)
        # print(url_re)
        # st.write(url_re)