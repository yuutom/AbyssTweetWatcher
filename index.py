import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
from util.csv_util import CSVUtilClass
import csv

today = '2022年8月1日'
st.subheader('更新日：{}'.format(today))

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

df = pd.DataFrame(
    count_list,
    word_list
)
st.subheader('今日のトレンドワード')
st.bar_chart(df)

text_score_list = []
with open('tweet_ranking.csv', encoding='utf_8_sig', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        text_score_list.append([row[0], row[1]])
text_score_list = text_score_list[:7]

st.subheader('今日の人気ツイート')
html_links = []
with open('html.csv', encoding='utf_8_sig', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        html_links.append(row[0])

for html_link in html_links:
    stc.html(html_link)